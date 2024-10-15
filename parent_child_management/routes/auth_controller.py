from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.orm_setup import get_session

from schemas.parents_schema import RegisterRequest, LoginRequest
from services.create_new_parent import create_new_parent
from services.account_verification import account_verification
from services.authenticate_parent import authenticate_parent

router = APIRouter()

@router.post("/register", tags=["auth"])
async def register_parent(request: RegisterRequest, session: Session = Depends(get_session)):
    return create_new_parent(request, session)

@router.get("/verify-account", tags=["auth"])
async def verify_account(parent_id: int, session: Session = Depends(get_session)):
    return account_verification(parent_id, session)

@router.post("/login", tags=["auth"])
async def login(request: LoginRequest, session: Session = Depends(get_session)):
    return authenticate_parent(request, session)

