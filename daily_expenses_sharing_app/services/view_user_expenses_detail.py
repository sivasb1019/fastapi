from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from models.expenses import Expense, Split
# from schemas.expense_schema import ExpenseList, Split

# Define a function to view a parent's children data
def view_user_expenses_detail(current_user, db: Session):
    try:
        # Fetch the expenses data based on the current user's ID
        user_id = current_user.user_id
        expenses = (db.query(Expense).options(joinedload(Expense.splits.and_(Split.user_id == user_id)))
                    .filter(Expense.user_id == user_id).all())

        # If the expense data is not found, raise a 404 Not Found exception
        if not expenses:
            raise HTTPException(status_code=404, detail="No expenses found for this user")
        
        return expenses
    
    except Exception as e:
        # If any exception occurs, roll back the database transaction and raise a 400 Bad Request exception
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        # Close the database session
        db.close()