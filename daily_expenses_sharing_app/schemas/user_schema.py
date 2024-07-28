from pydantic import BaseModel, EmailStr

class UserData(BaseModel):
    email: EmailStr
    name: str
    mobile: str

class UserCreate(UserData):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserList(UserData):
    id: int

    class Config:
        from_attributes = True
