from fastapi import HTTPException, status

from OtpValidation.utils.get_user import get_user
from OtpValidation.utils.password_auth import hash_password

 
def modify_password(credentials, current_user, db):
     if credentials.email != current_user.email:
          raise HTTPException(
               status_code=status.HTTP_403_FORBIDDEN,
               detail="Invalid operation: You are attempting to change the password for an unauthorized user."
               )
     user = get_user(current_user.email, db)
     user.password = hash_password(credentials.new_password)
     db.commit()
     return {"message": f"Password changed successfully for '{current_user.email}'"}
