from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.get_session import get_session
from utils.get_db import get_db
from schema.openingbalance import OpeningBalance
from services.get_expensefund_opening_balance import get_expensefund_opening_balance
from services.get_common_opening_balance import get_common_opening_balance

router = APIRouter(tags=["opening_balance"])

@router.get("/expensefund_opening_balance", response_model=OpeningBalance)
async def expensefund_opening_balance(input_date: date,
                                    session1: Session = Depends(get_session), 
                                    session2: Session = Depends(get_db)):
    return get_expensefund_opening_balance(input_date, session1, session2)

@router.get("/common_opening_balance", response_model=OpeningBalance)
async def common_opening_balance(input_date: date,
                                 session1: Session = Depends(get_session), 
                                 session2: Session = Depends(get_db)):
    return get_common_opening_balance(input_date, session1, session2)