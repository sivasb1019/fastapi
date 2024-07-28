from fastapi import HTTPException, status

from OtpValidation.models.UserTable import UserTable
from OtpValidation.utils.password_auth import hash_password

def create_new_user(user_data, db):
    new_user = UserTable(email=user_data.email, password=hash_password(user_data.password))
    try:
          db.add(new_user)
          db.commit()
    except:
         raise HTTPException(
              status_code=status.HTTP_208_ALREADY_REPORTED,
              detail=f"Given mail id '{user_data.email}' already exist"
              )

    return {"message": f"Success! New user created from email, '{user_data.email}'"}