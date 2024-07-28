from datetime import date
from pydantic import BaseModel

class Details(BaseModel):
    message : str

class AccountCreditDetails(BaseModel):
    id: int
    date: date
    type: str
    deposit_mode: str
    reason: str
    advance_receipt_no: str | None = None
    amount: float
    remaining_balance: float




