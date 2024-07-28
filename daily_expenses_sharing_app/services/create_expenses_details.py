from fastapi import HTTPException

from models.expenses import Expense, Split
from utils.get_user import get_user
from utils.notify_user import notify_user


def create_expenses_details(request, background_tasks, current_user, db):
    try:
        # Fetch the user data based on the current user's ID and email
        user_id = current_user.user_id
        user = get_user({"id": user_id, "email": current_user.email}, db)

        # If the user is not found, raise a 404 Not Found exception
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Create a new expense record
        new_expense = Expense(
            description=request.description,
            amount=request.amount,
            split_method=request.split_method,
            user_id=user_id
        )
        
        # db.add(new_expense)
        # db.commit()
        # db.refresh(new_expense)
        
        participants = len(request.splits)
        if participants == 0:
            raise HTTPException(status_code=400, detail="No participants provided for equal split.")

        # Handle splits based on the expense split_method
        if request.split_method == "equal":
            split_amount = new_expense.amount / participants
            for split in request.splits:
                user_instance = get_user({"id": split.user_id}, db)
                if not user_instance:
                    raise HTTPException(status_code=404, detail="User not found")

                new_split = Split(
                    percentage=None,
                    exact_amount=split_amount,
                    expense_id=new_expense.expense_id,
                    user_id=split.user_id,
                    created_by=user_id
                )
                new_expense.splits.append(new_split)

                # Add a background task to notify the admin about the new expense
                background_tasks.add_task(notify_user, user.name, user_instance.name, user_instance.email)
                # db.add(new_split)

        elif request.split_method == "exact":
            total_exact_amount = sum(split.exact_amount for split in request.splits)
            if total_exact_amount != new_expense.amount:
                raise HTTPException(status_code=400, detail="The total exact amounts do not match the expense amount.")
            for split in request.splits:
                user_instance = get_user({"id": split.user_id}, db)
                if not user_instance:
                    raise HTTPException(status_code=404, detail="User not found")
                new_split = Split(
                    percentage=None,
                    exact_amount=split.exact_amount,
                    expense_id=new_expense.expense_id,
                    user_id=split.user_id,
                    created_by=user_id
                )
                new_expense.splits.append(new_split)

                # Add a background task to notify the admin about the new expense
                background_tasks.add_task(notify_user, user.name, user_instance.name, user_instance.email)

                # db.add(new_split)

        elif request.split_method == "percentage":
            total_percentage = sum(split.percentage for split in request.splits)
            if total_percentage != 100:
                raise HTTPException(status_code=400, detail="Percentages must add up to 100%.")
            for split in request.splits:
                user_instance = get_user({"id": split.user_id}, db)
                if not user_instance:
                    raise HTTPException(status_code=404, detail="User not found")
                split_amount = (split.percentage / 100) * new_expense.amount
                new_split = Split(
                    percentage=split.percentage,
                    exact_amount=None,
                    expense_id=new_expense.expense_id,
                    user_id=split.user_id,
                    created_by=user_id
                )
                new_expense.splits.append(new_split)

                # Add a background task to notify the admin about the new expense
                background_tasks.add_task(notify_user, user.name, user_instance.name, user_instance.email)
                # db.add(new_split)

        else:
            raise HTTPException(status_code=400, detail="Invalid expense split_method. Use 'equal', 'exact', or 'percentage'.")
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)

        # db.commit()
        return {"message": f"New Expense created with id: {new_expense.expense_id}"}
    
    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Close the database session
        db.close()
