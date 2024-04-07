from datetime import datetime, timezone, timedelta

from jose import jwt, JWTError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials

from security_with_jwt.database import get_session
from security_with_jwt.schemas.auth_schemas import TokenData
from security_with_jwt.services.user_services import get_user
from security_with_jwt.utils import verify_password, bearer_scheme
from security_with_jwt.utils import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES




def authenticate_user(username, password, db):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
    

def generate_access_token(username, password, db):
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "bearer"}
        )
    payload = {
        "user_id": user.user_id, 
        "username": user.username,
        "role": user.role
        }
    access_token = create_access_token(data=payload)
    return {"access_token": access_token, "token_type": "bearer"}


def create_access_token(data: dict):
    to_encode = data.copy()
    if ACCESS_TOKEN_EXPIRE_MINUTES:
        expire_minutes = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    else:
        expire_minutes = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire_minutes})
    created_jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return created_jwt_token


def verify_access_token(token: str, credential_exceptions: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise credential_exceptions
        token_data = TokenData(user_id=user_id,
                               username=payload.get("username"),
                               role=payload.get("role"))
    except JWTError:
        raise credential_exceptions
    return token_data
    

def get_current_user(token: HTTPAuthorizationCredentials = Security(bearer_scheme), db: Session = Depends(get_session)):
    credential_exceptions = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "bearer"}
    )
    token_data = verify_access_token(token.credentials, credential_exceptions)
    user = get_user(token_data.username, db)
    if not user:
        raise credential_exceptions
    return token_data

