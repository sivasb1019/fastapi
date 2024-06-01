from datetime import date
from pydantic import BaseModel

class Details(BaseModel):
    message : str

class DailyLogDetails(BaseModel):
    id: int
    sales_type: str
    sales_code: str
    date: date
    bill_no: str
    customer_type: str
    bill_value: int
    amount: float | None = None
    advance_receipt_no: str | None = None
    advance_customer_name: str | None = None
    advance_receipt_amount: float | None = None
    pending_balance: float



