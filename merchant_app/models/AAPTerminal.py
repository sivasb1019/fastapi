from sqlalchemy import Column, Integer, String
from Database.db_config import Base

class AAPTerminal(Base):
    __tablename__ = 'aap_terminal'

    Id = Column(Integer, primary_key=True)
    Branch_Id = Column(String(50), nullable=False)
    Branch_Name = Column(String(50), nullable=False)
    Mobile_No = Column(String(50), nullable=False)
    Sequence_No = Column(String(50), nullable=False)
