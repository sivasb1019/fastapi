from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, func
from databases.db_setup import Base

class UserTable(Base):
    __tablename__ = "user_table"

    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Integer, nullable=False)
    otp = Column(String)
    otp_time = Column(Integer)
    login_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)