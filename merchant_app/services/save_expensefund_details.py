from fastapi.exceptions import HTTPException
from models.ExpenseFund import  ExpenseFund
from utils.get_id import get_id

def save_expensefund_details(requestList, session1, session2):
    try:
        for request in requestList:
            session_data = get_id(session2)
            ExpenseFund_instance = session1.query(ExpenseFund).filter(ExpenseFund.Id == request.id).first()
            if ExpenseFund_instance:
                ExpenseFund_instance.Expense_Fund_Details = request.expense_fund_details
                ExpenseFund_instance.Amount = request.amount
                ExpenseFund_instance.Balance = request.balance
            else:
                ExpenseFund_instance = ExpenseFund(
                    Date = request.date,
                    Expense_Fund_Details = request.expense_fund_details,
                    Amount = request.amount,
                    Balance = request.balance,
                    Branch_Id = session_data.get("branch_id"),
                    Merchant_Id = session_data.get("merchant_id")
                )
                session1.add(ExpenseFund_instance)
            session1.commit()
            session1.refresh(ExpenseFund_instance)
            session1.close()
        return {"message": "ExpenseFund details added successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


