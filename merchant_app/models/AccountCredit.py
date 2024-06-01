from sqlalchemy import Column, Integer, Float, String, Date, func
from Database.db_config import Base

class AccountCredit(Base):
    __tablename__ = 'account_credit'

    Id = Column(Integer, primary_key=True)
    Date = Column(Date, nullable=False)
    Type = Column(String(50))
    Deposit_Mode = Column(String(50))
    Reason = Column(String(50))
    PreOrder_Receipt_No = Column(String(20))
    Amount = Column(Float, nullable=False)
    Remaining_Balance = Column(Float, nullable=False)
    Branch_Id = Column(String(50), nullable=False)
    Merchant_Id = Column(String(50), nullable=False)

