from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.get_session import get_session
from utils.get_db import get_db
from schema.accountcredit import Details, AccountCreditDetails
from services.save_accountcredit_details import save_accountcredit_details
from services.get_accountcredit_details import get_accountcredit_details

router = APIRouter(tags=["accountcredit"])

@router.post("/save_AccountCredit", response_model=Details)
async def save_accountcredit(requestList: list[AccountCreditDetails], 
                           session1: Session = Depends(get_session),
                           session2: Session = Depends(get_db)):
    return save_accountcredit_details(requestList, session1, session2)

@router.get("/get_AccountCredit")
async def get_accountcredit(branch_id: str, history_type: int | None = None,
                          start_date: date | None = None, end_date: date | None = None,
                          session1: Session = Depends(get_session),
                          session2: Session = Depends(get_db)):
    return get_accountcredit_details(branch_id, history_type, start_date, end_date, session1, session2)
