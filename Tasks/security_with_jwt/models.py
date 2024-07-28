from sqlalchemy import Column, String, Integer, Boolean
from security_with_jwt.database import Base

class UserTable(Base):
    __tablename__ = "user_table"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
    active = Column(Boolean, default=True)