from fastapi import Security, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from utils.get_session import get_session
from utils.jwt_handling import verify_token
from utils.get_user import get_user

bearer_scheme = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Security(bearer_scheme), db: Session = Depends(get_session)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail=f"Could not validate credentials",
                                         headers={"WWW-Authenticate": "bearer"})
    token_data = verify_token(token.credentials, credential_exception)
    user = get_user(token_data.email, db)
    if not user:
        raise credential_exception
    return token_data
