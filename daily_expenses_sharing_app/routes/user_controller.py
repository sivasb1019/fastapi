from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.orm_setup import get_session

from schemas.user_schema import UserCreate, UserLogin
from services.create_new_user import create_new_user
from services.authenticate_user import authenticate_user
from schemas.user_schema import UserList
from utils.get_current_user import get_current_user
from services.get_user_data import get_user_data

router = APIRouter(prefix="/user")

@router.post("/create-user", tags=["auth"])
async def create_user(request: UserCreate, session: Session = Depends(get_session)):
    return create_new_user(request, session)

@router.post("/login-user", tags=["auth"])
async def login(request: UserLogin, session: Session = Depends(get_session)):
    return authenticate_user(request, session)

@router.get("/get-user/me", tags=["user"], response_model=UserList)
async def get_user(current_user: object = Depends(get_current_user), session: Session = Depends(get_session)):
    return get_user_data(current_user, session)

