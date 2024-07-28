from passlib.context import CryptContext

# Initialize a CryptContext for password hashing and verification
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a plaintext password
def hash_password(password):
    return pwd_context.hash(password)

# Verify if a plaintext password matches a hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
