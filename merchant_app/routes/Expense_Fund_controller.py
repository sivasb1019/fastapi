from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.get_session import get_session
from utils.get_db import get_db
from schema.expensefund import Details, ExpenseFundDetails
from services.save_expensefund_details import save_expensefund_details
from services.get_expensefund_details import get_expensefund_details

router = APIRouter(tags=["expensefund"])

@router.post("/save_ExpenseFund", response_model=Details)
async def save_expensefund(requestList: list[ExpenseFundDetails],
                           session1: Session = Depends(get_session),
                           session2: Session = Depends(get_db)):
    return save_expensefund_details(requestList, session1, session2)

@router.get("/get_expensefund")
async def get_expensefund(branch_id: str, history_type: int | None = None,
                          start_date: date | None = None, end_date: date | None = None,
                          session1: Session = Depends(get_session),
                          session2: Session = Depends(get_db)):
    return get_expensefund_details(branch_id, history_type, start_date, end_date, session1, session2)