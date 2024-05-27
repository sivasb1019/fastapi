from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user_schemas import CreateUser, Role
from schemas.auth_schemas import TokenData
from services.create_new_user import create_new_user
from services.set_activity_status import set_active_status
from services.delete_users import delete_users
from utils.get_current_user import get_current_user
from utils.get_session import get_session

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/create_user")
async def create_user(user_data: CreateUser, role: Role,
                      current_user: TokenData = Depends(get_current_user), 
                      session: Session = Depends(get_session)):
    return create_new_user(user_data, role, current_user, session)

@router.put("/update_status")
async def update_status(user_id: int, activity_status: bool,
                        current_user: TokenData = Depends(get_current_user),
                        session: Session = Depends(get_session)):
    return set_active_status(user_id, activity_status, current_user, session)

@router.put("/remove_user")
async def remove_user(user_id: int, 
                      current_user: TokenData = Depends(get_current_user),
                      session: Session = Depends(get_session)):
    return delete_users(user_id, current_user, session)