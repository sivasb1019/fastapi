from passlib.context import CryptContext

# Create a CryptContext instance for password hashing and verification
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define a function to hash a password
def hash_password(password):
    return pwd_context.hash(password)

# Define a function to verify a password against a hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)