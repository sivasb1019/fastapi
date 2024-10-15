from fastapi import status, HTTPException

from utils.get_parent import get_parent
from utils.jwt_handling import create_token
from utils.password_auth import verify_password
from schemas.auth_schema import Token

def authenticate_parent(credentials, db):
    # Define an HTTPException for invalid credentials
    credentials_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                          detail="Invalid Credentials",
                                          headers={"WWW-Authenticate": "bearer"})
    
    # Query the database to find the parent by email
    parent = get_parent({"email": credentials.email}, db)
    
    # Check if the parent exists, is active, and the password is correct
    if not parent or not parent.is_active or not verify_password(credentials.password, parent.password):
        raise credentials_exception
    
    # Create a JWT token for the authenticated parent
    jwt_token = create_token(data={"parent_id": parent.id, "email": parent.email, "is_active": parent.is_active})
    
    # Return a Token object with the parent's name, token, and type
    return Token(name=parent.firstname, is_active=parent.is_active, access_token=f"Bearer {jwt_token}", token_type="bearer")
