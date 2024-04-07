from enum import Enum
from pydantic import BaseModel, EmailStr


class Role(Enum):
    ADMIN = "Admin"
    USER = "User"
    

class UserRequest(BaseModel):
    username: str
    name: str
    email: EmailStr


class CreateUserRequest(UserRequest):
    password: str


class UserData(UserRequest):
    user_id: int
    role: str


class UpdateUserRequest(BaseModel):
    name: str | None = None
    email: EmailStr | None = None