from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user_schemas import CreateUser, UpdatePasswordRequest
from schemas.auth_schemas import TokenData
from services.user_sign_up import user_sign_up
from services.modify_password import modify_password
from utils.get_current_user import get_current_user
from utils.get_session import get_session

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/sign_up")
async def sign_up(user_data: CreateUser, session: Session = Depends(get_session)):
    return user_sign_up(user_data, session)

@router.put("/update_password")
async def update_password(credentials: UpdatePasswordRequest, 
                          current_user: TokenData = Depends(get_current_user),
                          session: Session = Depends(get_session)):
    return modify_password(credentials, current_user, session)