from fastapi import status, HTTPException

from utils.get_user import get_user
from utils.jwt_handling import create_token
from utils.password_auth import verify_password
from schemas.auth_schema import Token

def authenticate_user(credentials, db):
    # Define an HTTPException for invalid credentials
    credentials_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                          detail="Invalid Credentials",
                                          headers={"WWW-Authenticate": "bearer"})
    
    # Query the database to find the user by email
    user = get_user({"email": credentials.email}, db)
    
    # Check if the user exists, is active, and the password is correct
    if not user or not user.is_active or not verify_password(credentials.password, user.password):
        raise credentials_exception
    
    # Create a JWT token for the authenticated user
    jwt_token = create_token(data={"user_id": user.id, "email": user.email, "is_active": user.is_active})
    
    # Return a Token object with the user's name, token, and type
    return Token(name=user.name, is_active=user.is_active, access_token=f"Bearer {jwt_token}", token_type="bearer")
