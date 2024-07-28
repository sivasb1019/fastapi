from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import Master_controller, Book_Type_controller, PreOrder_Book_controller
from routes import Opening_Balance_controller, Account_Credit_controller, Daily_Log_controller, Expense_Fund_controller
import uvicorn


app = FastAPI(docs_url="/api/v21/docs",
              openapi_url="/api/v21/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.include_router(Master_controller.router,prefix="/api/v21/master")
app.include_router(Book_Type_controller.router,prefix="/api/v21/book_type")
app.include_router(Opening_Balance_controller.router,prefix="/api/v21/opening_balance")
app.include_router(PreOrder_Book_controller.router,prefix="/api/v21/preorderbook")
app.include_router(Daily_Log_controller.router,prefix="/api/v21/daily_log")
app.include_router(Account_Credit_controller.router,prefix="/api/v21/account_credit")
app.include_router(Expense_Fund_controller.router,prefix="/api/v21/expense_fund")


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)



