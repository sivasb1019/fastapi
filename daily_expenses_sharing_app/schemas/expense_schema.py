from pydantic import BaseModel
from schemas.user_schema import UserList

class SplitBase(BaseModel):
    user_id: int
    percentage: float | None = None
    exact_amount: float | None = None


class Split(SplitBase):
    split_id: int
    # user: UserList

    class Config:
        from_attributes = True

class ExpenseBase(BaseModel):
    description: str
    split_method: str
    amount: float

class CreateExpense(ExpenseBase):
    splits: list[SplitBase]

class ExpenseList(ExpenseBase):
    expense_id: int
    user_id: int
    # owner: UserList
    splits: list[Split]

    class Config:
        from_attributes = True

from datetime import date
class ExcludeSplits(BaseModel):
    pass

class ExcludeExpense(BaseModel):
    created_at: date
    splits: list[ExcludeSplits]