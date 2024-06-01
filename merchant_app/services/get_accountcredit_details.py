from datetime import datetime
from fastapi import HTTPException
from models.AccountCredit import AccountCredit
from utils.get_id import get_id
from utils.get_day import get_day

def get_accountcredit_details(branch_id, history_type, start_date, end_date, session1, session2):
    try:
        session_data = get_id(session2)
        if branch_id != '0':
            if history_type:
                start_date = get_day(history_type)
                end_date = start_date if history_type < 3 else datetime.now().date()

            data = session1.query(AccountCredit).filter(AccountCredit.Branch_Id == branch_id,
                                                      AccountCredit.Merchant_Id == session_data.get("merchant_id"),
                                                      AccountCredit.Date >= start_date, AccountCredit.Date <= end_date).all()
        else:
            if history_type:
                start_date = get_day(history_type)
                end_date = start_date if history_type < 3 else datetime.now().date()

            data = session1.query(AccountCredit).filter(AccountCredit.Date >= get_day(history_type),
                                                      AccountCredit.Merchant_Id == session_data.get("merchant_id")).all()
            
        
        session1.close()
        session2.close()
        return data
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
