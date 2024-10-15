from pydantic import BaseModel, EmailStr
from datetime import date

# Define a LoginRequest model to handle user login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Define a RegisterRequest model to handle user registration
# This inherits from the LoginRequest model and adds additional fields
class RegisterRequest(LoginRequest):
    firstname: str
    middlename: str | None = None
    lastname: str | None = None


# Define a ListParent model to represent a parent's information
class ListParent(BaseModel):
    id: int
    firstname: str | None = None
    middlename: str | None = None
    lastname: str | None = None
    email: EmailStr
    profile_photo: str | None = None
    age: int | None = None
    dob: date | None = None
    mobile: str | None = None
    address_line_1: str | None = None
    address_line_2: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    pincode: str | None = None

    class Config:
        from_attributes = True