from sqlalchemy import Column, Integer, String
from Database.db_config import Base

class DayInfo(Base):
    __tablename__ = 'day_info'

    Id = Column(Integer, primary_key=True)
    Type = Column(String(20), nullable=False)