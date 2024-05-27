from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    role: int
    is_active: bool
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int
    role: int
    email: EmailStr