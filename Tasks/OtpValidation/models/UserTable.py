from sqlalchemy import Column, String, Integer, TIMESTAMP, func
from OtpValidation.database.orm_setup import Base

class UserTable(Base):
    __tablename__ = "user_table"

    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    login_time = Column(TIMESTAMP(timezone=True), 
                        server_default=func.now(), onupdate=func.now())
    otp = Column(String)
    otp_time = Column(Integer)