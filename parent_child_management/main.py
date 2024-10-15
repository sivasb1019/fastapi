from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_controller, parent_controller
import uvicorn

# Create a FastAPI instance to build the web application
app = FastAPI()

# Add CORS middleware to allow cross-origin requests from any origin
# This is necessary for the frontend application to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

# Include the auth and parent controllers in the application
# The auth controller handles user authentication and registration
# The parent controller handles operations related to parents and their children
app.include_router(auth_controller.router, prefix="/api/v1/auth")
app.include_router(parent_controller.router, prefix="/api/v1/parent")

# Run the application using Uvicorn, a high-performance ASGI server
# This will start the server and make the application available at http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', reload=True)