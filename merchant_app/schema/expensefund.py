from datetime import date
from pydantic import BaseModel

class Details(BaseModel):
    message : str

class ExpenseFundDetails(BaseModel):
    id: int
    date: date
    expense_fund_details: str
    amount: float
    balance: float
    
