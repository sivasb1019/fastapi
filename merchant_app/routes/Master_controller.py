from fastapi import APIRouter, Depends

from services.get_customertype_details import get_customertype_details
from services.get_paymenttype_details import get_paymenttype_details
from services.get_salestype_details import get_salestype_details
from services.get_upitype_details import get_upitype_details
from services.get_depositmode_details import get_depositmode_details
from services.get_deposittype_details import get_deposittype_details
from services.get_booktype_info import get_booktype_info
from services.get_day_info import get_day_info
from services.get_aap_terminal import get_aap_terminal
from utils.get_session import get_session
from utils.get_db import get_db


router = APIRouter(tags=["master"])

@router.get("/get_BookTypeInfo")
async def get_BookType(session = Depends(get_session)):
    return get_booktype_info(session)

@router.get("/get_CustomerType")
async def get_customertype(session = Depends(get_session)):
    return get_customertype_details(session)

@router.get("/get_PaymentType")
async def get_paymenttype(session = Depends(get_session)):
    return get_paymenttype_details(session)

@router.get("/get_SalesType")
async def get_salestype(session = Depends(get_session)):
    return get_salestype_details(session)

@router.get("/get_UPIType")
async def get_upitype(session = Depends(get_session)):
    return get_upitype_details(session)

@router.get("/get_DepositMode")
async def get_depositmode(session = Depends(get_session)):
    return get_depositmode_details(session)

@router.get("/get_DepositType")
async def get_deposittype(session = Depends(get_session)):
    return get_deposittype_details(session)

@router.get("/get_DayInfo")
async def get_DayInfo(session = Depends(get_session)):
    return get_day_info(session)

@router.get("/get_AAPTerminal")
async def get_AAPTerminal(session1 = Depends(get_session), session2 = Depends(get_db)):
    return get_aap_terminal(session1, session2)
