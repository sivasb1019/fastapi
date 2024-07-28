from pydantic import BaseModel, EmailStr


class UserInfo(BaseModel):
    email: EmailStr

class CreateUser(UserInfo):
    password: str

class UpdatePasswordRequest(UserInfo):
    new_password: str

class GenerateOTP(CreateUser):
    pass

class ValidateOTP(BaseModel):
    email: EmailStr
    otp: str

