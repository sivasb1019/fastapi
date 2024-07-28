from sqlalchemy import Column, Integer, String, Date, Float, func
from Database.db_config import Base


class DailyLog(Base):
    __tablename__ = 'daily_log'
    
    Id = Column(Integer, primary_key=True)
    Sales_Type = Column(String(20), nullable=False)
    Sales_Code = Column(String(20), nullable=False)
    Date = Column(Date, nullable=False)
    Bill_No = Column(String(250), unique=True, index=True, nullable=False)
    Customer_Type = Column(String(20), nullable=False)
    Bill_Value = Column(Integer, nullable=False)
    Amount = Column(Float)
    PreOrder_Receipt_No = Column(String(20))
    PreOrder_Customer_Name = Column(String(20))
    PreOrder_Receipt_Amount = Column(Float)
    Pending_Balance = Column(Float, nullable=False)
    Branch_Id = Column(String(50), nullable=False)
    Merchant_Id = Column(String(50), nullable=False)