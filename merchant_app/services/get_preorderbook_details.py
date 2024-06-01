from datetime import datetime
from fastapi import HTTPException
from models.PreOrderBook import PreOrderBook
from utils.get_id import get_id
from utils.get_day import get_day

def get_preorderbook_details(branch_id, history_type, start_date, end_date, session1, session2):
    try:
        session_data = get_id(session2)
        if branch_id != '0':
            if history_type:
                start_date = get_day(history_type)
                end_date = start_date if history_type < 3 else datetime.now().date()

            data = session1.query(PreOrderBook).filter(PreOrderBook.Branch_Id == branch_id,
                                                       PreOrderBook.Merchant_Id == session_data.get("merchant_id"),
                                                       PreOrderBook.Date >= start_date, PreOrderBook.Date <= end_date).all()
        else:
            if history_type:
                start_date = get_day(history_type)
                end_date = start_date if history_type < 3 else datetime.now().date()

            data = session1.query(PreOrderBook).filter(PreOrderBook.Date >= get_day(history_type),
                                                       PreOrderBook.Merchant_Id == session_data.get("merchant_id")).all()

        session1.close()
        session2.close()
        return data
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
