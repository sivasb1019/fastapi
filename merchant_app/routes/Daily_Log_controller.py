from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.get_session import get_session
from utils.get_db import get_db
from schema.dailylog import Details, DailyLogDetails
from services.save_dailylog_details import save_dailylog_details
from services.get_dailylog_details import get_dailylog_details

router = APIRouter(tags=["dailylog"])

@router.post("/save_DailyLog", response_model=Details)
async def save_dailylog(requestList: list[DailyLogDetails],
                           session1: Session = Depends(get_session),
                           session2: Session = Depends(get_db)):
    return save_dailylog_details(requestList, session1, session2)

@router.get("/get_dayBook")
async def get_dailylog(branch_id: str, history_type: int | None = None,
                          start_date: date | None = None, end_date: date | None = None,
                          session1: Session = Depends(get_session),
                          session2: Session = Depends(get_db)):
    return get_dailylog_details(branch_id, history_type, start_date, end_date, session1, session2)


