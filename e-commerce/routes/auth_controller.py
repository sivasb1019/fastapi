from fastapi import APIRouter, Depends

from utils.get_session import get_session
from services.otp_request import otp_request
from services.generate_access_token import generate_access_token
from schemas.response_schemas import Response_Message
from schemas.user_schemas import OTP_Request, OTP_Validation
from schemas.auth_schemas import Token


router = APIRouter(prefix="/auth", tags=["authorization"])

@router.post("/generate-otp", response_model=Response_Message)
async def generate_otp(request: OTP_Request, session= Depends(get_session)):
    return otp_request(request, session)

@router.post("/generate-token", response_model=Token)
async def generate_token(credentials: OTP_Validation, session = Depends(get_session)):
    return generate_access_token(credentials, session)