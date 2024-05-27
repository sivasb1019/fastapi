from time import time

from fastapi import HTTPException, status

from utils.get_user import get_user
from utils.password_auth import verify_password
from utils.get_otp import get_otp
from utils.send_otp import send_otp

def otp_request(credentials, db):
     user = get_user(credentials.email, db)
     if not user or not verify_password(credentials.password, user.password):
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Invalid Credentials"
               )
     otp = get_otp()
     send_otp(credentials.email, otp)
     user.otp = otp
     user.otp_time = time()
     db.commit()

     return {"message": f"OTP generated succussfully to '{user.email}'",
             "time_limit":"OTP time limit is 1 minute"}
