from sqlalchemy import Column, Integer, Float, String, Date, func
from Database.db_config import Base


class PreOrderBook(Base):
    __tablename__ = 'preorder_book'

    Id = Column(Integer, primary_key=True)
    Date  = Column(Date, nullable=False)
    Receipt_No = Column(String(250), unique=True, nullable=False)
    Customer_Name  = Column(String(50), nullable=False)
    Phone_No  = Column(String(20), nullable=False)
    Amount = Column(Float)
    Payment_Type = Column(String(50))
    Status = Column(String(50),nullable=False)
    Customer_Type  = Column(String(50))
    Branch_Id = Column(String(50), nullable=False)
    Merchant_Id = Column(String(50), nullable=False)
