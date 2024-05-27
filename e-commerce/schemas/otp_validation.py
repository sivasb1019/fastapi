from pydantic import BaseModel, EmailStr


class OTP_Request(BaseModel):
    email: EmailStr
    password: str

class OTP_Validation(OTP_Request):
    otp: str