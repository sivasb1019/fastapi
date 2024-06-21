from fastapi import FastAPI
import uvicorn

from routes import user_controller

app = FastAPI()

# Include the user_controller router from routes module
app.include_router(user_controller.router)

if __name__ == "__main__":
    # Run the FastAPI application using uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
