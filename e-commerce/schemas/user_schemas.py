from enum import Enum
from pydantic import BaseModel, EmailStr


class Role(Enum):
    ADMIN = "Admin"
    SELLER = "Seller"

class UserInfo(BaseModel):
    email: EmailStr

class CreateUser(UserInfo):
    password: str

class UpdatePasswordRequest(CreateUser):
    new_password: str
    confirm_new_password: str

class OTP_Request(CreateUser):
    pass

class OTP_Validation(UserInfo):
    otp: str