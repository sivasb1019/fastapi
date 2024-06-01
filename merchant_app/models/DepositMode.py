from sqlalchemy import Column, Integer, String
from Database.db_config import Base

class DepositMode(Base):
    __tablename__ = 'deposit_mode'

    Id = Column(Integer, primary_key=True)
    Type = Column(String(20), nullable=False)