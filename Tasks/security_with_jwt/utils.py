import os
from dotenv import load_dotenv

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, HTTPBearer

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

outh2_scheme = OAuth2PasswordBearer(tokenUrl="generate-token")

bearer_scheme = HTTPBearer()

# Hashing password function
def hash_password(password):
    return pwd_context.hash(password) 


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)