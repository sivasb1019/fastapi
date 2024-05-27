import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

from fastapi import HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

from schemas.auth_schemas import TokenData

load_dotenv(override=True)

# Accessing SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES from .env file to authenticate JWT token
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def create_token(data:dict, expire = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    if expire:
        expire_minutes = datetime.now(timezone.utc) + timedelta(minutes=int(expire))
    else:
        expire_minutes = datetime.now(timezone.utc) + timedelta(minutes=10)
    to_encode.update({"exp": expire_minutes})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str, credential_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise credential_exception
        token_data = TokenData(user_id=user_id, role=payload.get("role"), email=payload.get("email"))
    except JWTError:
        raise credential_exception
    return token_data