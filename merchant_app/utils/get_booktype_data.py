from datetime import datetime
from fastapi import HTTPException
from utils.get_id import get_id
from utils.get_day import get_day


def get_booktype_data(book_type, branch_id, history_type, start_date, end_date, session1, session2):
    try:
        session_data = get_id(session2)

        if branch_id != '0':
            if history_type:
                start_date = get_day(history_type)
                end_date = start_date if history_type < 3 else datetime.now().date()

            data = session1.query(book_type).filter(book_type.Branch_Id == branch_id,
                                                    book_type.Merchant_Id == session_data.get("merchant_id"),
                                                    book_type.Date >= start_date, book_type.Date <= end_date).all()
        else:
            if history_type:
                start_date = get_day(history_type)
                end_date = start_date if history_type < 3 else datetime.now().date()

            data = session1.query(book_type).filter(book_type.Merchant_Id == session_data.get("merchant_id"),
                                                    book_type.Date >= start_date, book_type.Date <= end_date).all()
            
        
        session1.close()
        session2.close()
        return data
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

