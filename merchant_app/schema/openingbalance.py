from pydantic import BaseModel


class OpeningBalance(BaseModel):
    opening_balance: float