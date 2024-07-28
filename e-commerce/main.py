from fastapi import FastAPI
import uvicorn

from routes import auth_controller, user_controller, admin_controller, seller_controller, customer_controller

app = FastAPI(title="Ecommerce API")

app.include_router(user_controller.router)
app.include_router(auth_controller.router)
app.include_router(admin_controller.router)
app.include_router(seller_controller.router)
app.include_router(customer_controller.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)