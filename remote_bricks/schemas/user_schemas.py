from pydantic import BaseModel, EmailStr

# Define Pydantic models for data validation
class Login(BaseModel):
    email: EmailStr
    password: str

class User(Login):
    username: str

class LinkID(BaseModel):
    user_id: str
    linked_id: str

class JoinResponse(BaseModel):
    _id: int
    email: str
    username: str
    linked_ids: list[str]  # Define linked_ids as a list of strings
