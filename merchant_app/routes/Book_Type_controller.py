from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.get_session import get_session
from utils.get_db import get_db
from services.get_booktype_details import get_booktype_details
from services.downloadbooks import downloadbooks

router = APIRouter(tags=["booktype"])

@router.get("/view_BookData")
async def view_BookData(book_type: str, branch_id: str, history_type: int | None = None,
                        start_date: date | None = None, end_date: date | None = None,
                        session1: Session = Depends(get_session),
                        session2: Session = Depends(get_db)):
    return get_booktype_details(book_type, branch_id, history_type, start_date, end_date, session1, session2)


@router.get("/download_book")
async def download_book(book_type: str, branch_id: str, history_type: int | None = None,
                        start_date: date | None = None, end_date: date | None = None,
                        session1: Session = Depends(get_session),
                        session2: Session = Depends(get_db)):
    return downloadbooks(book_type, branch_id, history_type, start_date, end_date, session1, session2)
