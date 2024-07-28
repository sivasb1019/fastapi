from fastapi import HTTPException, status

from utils.get_user import get_user
from utils.password_auth import verify_password, hash_password

 
def modify_password(credentials, current_user, db):
     if credentials.email != current_user.email:
          raise HTTPException(
               status_code=status.HTTP_403_FORBIDDEN,
               detail="Invalid operation: You are attempting to change the password for an unauthorized user."
               )
     user = get_user(current_user.email, db)
     if not verify_password(credentials.password, user.password):
          raise HTTPException(
               status_code=status.HTTP_403_FORBIDDEN,
               detail="Invalid password. Please verify your old password"
               )
     if credentials.new_password != credentials.confirm_new_password:
          raise HTTPException(
               status_code=status.HTTP_403_FORBIDDEN,
               detail="New password doesn't match. Please confirm your new password"
               )

     user.password = hash_password(credentials.new_password)
     db.commit()
     return {"message": f"Password changed successfully for '{current_user.email}'"}
