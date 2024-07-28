from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from OtpValidation.schemas.auth_schemas import Token
from OtpValidation.schemas.user_schemas import ValidateOTP
from OtpValidation.utils.get_session import get_session
from OtpValidation.services.generate_access_token import generate_access_token

route = APIRouter()

@route.post("/generate-token", tags=["Generate Token"], response_model=Token)
async def generate_token(credentials: ValidateOTP, session: Session = Depends(get_session)):
    return generate_access_token(credentials, session)