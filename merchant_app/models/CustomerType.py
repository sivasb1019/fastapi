from sqlalchemy import Column, Integer, String
from Database.db_config import Base

class CustomerType(Base):
    __tablename__ = 'customer_type'

    Id = Column(Integer, primary_key=True)
    Type = Column(String(20), nullable=False)