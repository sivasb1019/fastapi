from sqlalchemy import Column, Integer, String
from Database.db_config import Base

class UPIType(Base):
    __tablename__ = 'upi_type'

    Id = Column(Integer, primary_key=True)
    Type = Column(String(20), nullable=False)