import os
from dotenv import load_dotenv
from time import time

from fastapi import status, HTTPException

from utils.get_user import get_user
from utils.jwt_handling import create_token
from schemas.auth_schemas import Token

load_dotenv(override=True)

OTP_TIME_LIMIT = os.getenv("OTP_TIME_LIMIT")

def generate_access_token(credentials, db):
    credentials_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                          detail="Invalid Credentials",
                                          headers={"WWW-Authenticate": "bearer"})
    user = get_user(credentials.email, db)
    if not user or not user.is_active:
        raise credentials_exception
    
    otp_validate_time = time() - user.otp_time
    if int(OTP_TIME_LIMIT) < otp_validate_time:
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT,
                            detail="OTP time limit reached. Request a new OTP.")
    if user.otp != credentials.otp:
            raise credentials_exception
    jwt_token =  create_token(data={"user_id": user.user_id, "email": user.email, "role": user.role})
    return Token(role=user.role, is_active=user.is_active, access_token=f"Bearer {jwt_token}", token_type="bearer")