from datetime import date
from pydantic import BaseModel

class Details(BaseModel):
    message : str

class PreOrderBookDetails(BaseModel):
    id: int
    date: date
    receipt_no : str
    customer_name : str
    phone_no : str
    amount: float | None = None
    payment_type: str | None = None 
    status: str
    customer_type: str | None = None