from fastapi import FastAPI
import uvicorn

from OtpValidation.routes import auth_controller
from OtpValidation.routes import user_controller

app = FastAPI(title="OTP Validation")

app.include_router(auth_controller.route)
app.include_router(user_controller.route)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
