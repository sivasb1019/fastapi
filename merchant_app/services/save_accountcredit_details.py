from datetime import datetime, timedelta
from fastapi.exceptions import HTTPException
from models.AccountCredit import  AccountCredit
from utils.get_id import get_id


def save_accountcredit_details(requestList, session1, session2):
    try:
        for request in requestList:
            session_data = get_id(session2)
            AccountCredit_instance = session1.query(AccountCredit).filter(AccountCredit.Id == request.id).first()
            if AccountCredit_instance:
                AccountCredit_instance.Type = request.type
                AccountCredit_instance.Deposit_Mode = request.deposit_mode
                AccountCredit_instance.Reason = request.reason,
                AccountCredit_instance.PreOrder_Receipt_No = request.advance_receipt_no
                AccountCredit_instance.Amount = AccountCredit_instance.amount
                AccountCredit_instance.Remaining_Balance = request.remaining_balance
            else:
                AccountCredit_instance = AccountCredit(
                    Date = request.date,
                    Type = request.type,
                    Deposit_Mode = request.deposit_mode,
                    Reason = request.reason,
                    PreOrder_Receipt_No = request.advance_receipt_no,
                    Amount = request.amount,            
                    Remaining_Balance = request.remaining_balance,
                    Branch_Id = session_data.get("branch_id"),
                    Merchant_Id = session_data.get("merchant_id")
                )
                session1.add(AccountCredit_instance)
            session1.commit()
            session1.refresh(AccountCredit_instance)
            session1.close()

        return {"message": "Bank deposit details added succesfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




