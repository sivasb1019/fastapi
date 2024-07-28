from models.users import User
from schemas.auth_schema import TokenData

def get_token_data():
    return TokenData(parent_id=10, email="parentdemo@gmail.com", is_active=True)

def get_user():
    return User(id=10, name="Demo User", email="userdemo@gmail.com", mobile="7896541230", is_active=True, is_admin=False)

