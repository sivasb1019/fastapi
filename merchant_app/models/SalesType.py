from sqlalchemy import Column, Integer, String
from Database.db_config import Base

class SalesType(Base):
    __tablename__ = 'sales_type'

    Id = Column(Integer, primary_key=True)
    Type = Column(String(20), nullable=False)
    Code = Column(String(20), nullable=False)