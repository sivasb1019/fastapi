from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema.preorderbook import Details, PreOrderBookDetails
from utils.get_session import get_session
from utils.get_db import get_db
from services.save_preorderbook_details import save_preorderbook_details
from services.verify_receipt_number import verify_receipt_number
from services.get_preorderbook_details import get_preorderbook_details

router = APIRouter(tags=["preorderbook"])

@router.post("/save_PreOrderBook", response_model=Details)
async def save_preorderbook(requestList: list[PreOrderBookDetails],  
                            session1: Session = Depends(get_session),
                            session2: Session = Depends(get_db)):
    return save_preorderbook_details(requestList, session1, session2)

@router.post("/verify_PreOrderReceipt/{PreOrder_Receipt_No}")
async def verify_receipt(PreOrder_Receipt_No: str,
                         session1: Session = Depends(get_session),
                         session2: Session = Depends(get_db)):
    return verify_receipt_number(PreOrder_Receipt_No, session1, session2)

@router.get("/get_PreOrderBook")
async def get_preorderbook(branch_id: str, history_type: int | None = None,
                          start_date: date | None = None, end_date: date | None = None,
                          session1: Session = Depends(get_session),
                          session2: Session = Depends(get_db)):
    return get_preorderbook_details(branch_id, history_type, start_date, end_date, session1, session2)

