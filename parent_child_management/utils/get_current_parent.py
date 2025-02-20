from fastapi import Security, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database.orm_setup import get_session
from utils.jwt_handling import verify_token
from utils.get_parent import get_parent

# Define a bearer scheme for authentication
bearer_scheme = HTTPBearer()

# Define a function to get the current parent from the request
def get_current_parent(token: HTTPAuthorizationCredentials = Security(bearer_scheme), db: Session = Depends(get_session)):
    # Verify the token and get the token data
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail=f"Could not validate credentials",
                                         headers={"WWW-Authenticate": "bearer"})
    token_data = verify_token(token.credentials, credential_exception)

    # Fetch the parent data based on the token data
    parent = get_parent({"email": token_data.email}, db)
    
    # If the parent data is not found, raise a 401 Unauthorized exception
    if not parent:
        raise credential_exception
    
    return token_data