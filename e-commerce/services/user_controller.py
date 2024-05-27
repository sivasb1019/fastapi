from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from OtpValidation.schemas.user_schemas import CreateUser, GenerateOTP, UpdatePasswordRequest
from OtpValidation.schemas.auth_schemas import TokenData
from OtpValidation.services.create_new_user import create_new_user
from OtpValidation.services.access_otp import access_otp
from OtpValidation.services.modify_password import modify_password
from OtpValidation.utils.get_current_user import get_current_user
from OtpValidation.utils.get_session import get_session

route = APIRouter(prefix="/user")

@route.post("/create_user", tags=["Create user"], responses={400: {"description": "Password not match"}})
async def create_user(user_data: CreateUser, session: Session = Depends(get_session)):
    return create_new_user(user_data, session)
    
@route.post("/otp_generation", tags=["OTP generation"])
async def generate_otp(credentials: GenerateOTP, session: Session = Depends(get_session)):
    return access_otp(credentials, session)

@route.put("/update_password", tags=["Update Password"])
async def update_password(credentials: UpdatePasswordRequest, 
                          current_user: TokenData = Depends(get_current_user),
                          session: Session = Depends(get_session)):
    return modify_password(credentials, current_user, session)