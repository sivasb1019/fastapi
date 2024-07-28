from fastapi import HTTPException, status

from security_with_jwt.models import UserTable 
from security_with_jwt.utils import hash_password


def get_user(username, db):
    return db.query(UserTable).filter(UserTable.username == username).first()


def verify_user(username, db):
    user = get_user(username, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Username '{username}' not found"
        )
    return user


def create_new_user(user, role, db):
    hashed_password = hash_password(user.password)
    create_user = UserTable(username=user.username,
                            hashed_password=hashed_password,
                            name=user.name,
                            email=user.email,
                            role=role)
    try:
        db.add(create_user)
        db.commit()
    except:
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail=f"Given mail id {create_user.username} or {create_user.email} already exist"
        )
    
    return {"message": f"{create_user.role} id created successfully for {create_user.name}"}


def update_user_data(username, user_data, db):
    user = verify_user(username, db)
    try:
        if user_data.email:
            user.email = user_data.email
        if user_data.name:
            user.name = user_data.name
        db.commit()
    except:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"No data is provided"
        )
    
    return {"message": f"User '{user.username}' profile has been updated successfully"}


def set_user_active_status(user_id, active_status, admin, db):
    if admin.role != 'Admin':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User '{admin.username}' is unauthorized to modify activity status"
        )
    user = db.query(UserTable).filter(UserTable.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail=f"Given {user.role} id '{user_id}' not found"
        )
    user.active = active_status
    db.commit()
    return {"message": f"{user.username} active status is set to {active_status}"}
        