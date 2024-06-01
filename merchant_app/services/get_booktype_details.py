from fastapi import HTTPException
from utils.get_booktype import get_booktype
from utils.get_booktype_data import get_booktype_data

def get_booktype_details(book_type, branch_id, history_type, start_date, end_date, session1, session2):
    try:
        book_type = get_booktype(book_type)
        return get_booktype_data(book_type, branch_id, history_type, start_date, end_date, session1, session2)
         
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
