import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

from fastapi import HTTPException
from jose import jwt, JWTError

from schemas.auth_schema import TokenData

# Load environment variables from the .env file
load_dotenv(override=True)

# Accessing SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES from .env file to authenticate JWT token
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
INACTIVITY_TIMEOUT_SECONDS = os.getenv("INACTIVITY_TIMEOUT_SECONDS")

# Define a function to create a JWT token
def create_token(data:dict, expire = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    if expire:
        # Calculate the expiration time for the token
        expire_minutes = datetime.now(timezone.utc) + timedelta(minutes=int(expire))
    else:
        # Set a default expiration time of 10 minutes
        expire_minutes = datetime.now(timezone.utc) + timedelta(minutes=10)
        
    to_encode.update({"exp": expire_minutes})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Define a function to verify a JWT token
def verify_token(token: str, credential_exception: HTTPException):
    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        parent_id = payload.get("parent_id")
        if not parent_id:
            # If the parent ID is not present in the token, raise a credential exception
            raise credential_exception
        # Create a TokenData object from the token payload
        token_data = TokenData(parent_id=parent_id, email=payload.get("email"), is_active=payload.get("is_active"))

    except JWTError:
        # If there's an error decoding the token, raise a credential exception
        raise credential_exception
    
    return token_data