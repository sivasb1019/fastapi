from fastapi import HTTPException, status

from models.UserTable import UserTable
from utils.get_role import get_role
from utils.password_auth import hash_password

def create_new_user(user_data, role, current_user, db):
    if current_user.role != 1:
      raise HTTPException(
          status_code=status.HTTP_403_FORBIDDEN,
          detail="Invalid operation: Adding sellers are unauthorized for customers and sellers."
     )
    role = get_role(role.value)
    new_user = UserTable(email=user_data.email, role=role, password=hash_password(user_data.password))
    try:
          db.add(new_user)
          db.commit()
    except:
         raise HTTPException(
              status_code=status.HTTP_208_ALREADY_REPORTED,
              detail=f"Given mail id '{user_data.email}' already exist"
              )

    return {"message": f"Success! New user created from email, '{user_data.email}'"}