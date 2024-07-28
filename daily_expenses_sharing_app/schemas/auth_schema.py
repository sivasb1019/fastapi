from pydantic import BaseModel, EmailStr

# Define a Token model to represent the authentication token
class Token(BaseModel):
    name: str
    is_active: bool
    access_token: str
    token_type: str

# Define a TokenData model to represent the data contained in the authentication token
class TokenData(BaseModel):
    user_id: int
    email: EmailStr
    is_active: bool