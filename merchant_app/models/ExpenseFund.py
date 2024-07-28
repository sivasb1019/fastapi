from sqlalchemy import Column, Integer, Float, String, Date, func
from Database.db_config import Base

class ExpenseFund(Base):
    __tablename__ = 'expense_fund'

    Id = Column(Integer, primary_key=True)
    Date = Column(Date, nullable=False)
    Expense_Fund_Details = Column(String(300), nullable=False)
    Amount = Column(Float, nullable=False)
    Balance = Column(Float, nullable=False)
    Branch_Id = Column(String(50), nullable=False)
    Merchant_Id = Column(String(50), nullable=False)


