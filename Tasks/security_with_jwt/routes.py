from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session


from security_with_jwt.database import Base, engine, get_session
from security_with_jwt.schemas.user_schemas import UserData, CreateUserRequest, Role, UpdateUserRequest
from security_with_jwt.schemas.auth_schemas import Token, TokenData
from security_with_jwt.services.user_services import verify_user, create_new_user, set_user_active_status, update_user_data
from security_with_jwt.services.auth_services import generate_access_token, get_current_user

route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.post("/generate-token", tags=["Generate Token"], response_model=Token)
async def generate_token(username: str = Body(...), password: str = Body(...), db: Session = Depends(get_session)):
    return generate_access_token(username, password, db )

@route.get("/users/validate_user", tags=["User"], response_model=UserData)
async def validate_user(username: str, db: Session = Depends(get_session)):
    return verify_user(username, db)

@route.post("/users/create_user", tags=["User"], responses={208: {"description": "Already exist"}})
async def create_user(user: CreateUserRequest, role: Role, session: Session = Depends(get_session)):
    return create_new_user(user, role.value, session)


@route.put("/users/update_user", tags=["Authentication"], dependencies=[Depends(get_current_user)])
async def update_user(username: str, user_data: UpdateUserRequest | None = None, session: Session = Depends(get_session)):
    return update_user_data(username, user_data, session)


@route.put("/users/update_activity_status", tags=["Authentication"])
async def update_user_active_status(user_id: int, active: bool, admin: TokenData = Depends(get_current_user), session: Session = Depends(get_session)):
    return set_user_active_status(user_id, active, admin, session)

