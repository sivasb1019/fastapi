from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.orm_setup import Base

# Define the Parent model, which represents a parent in the system
class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    profile_photo = Column(String)
    firstname = Column(String, nullable=False)
    middlename = Column(String)
    lastname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    age = Column(Integer)
    dob = Column(Date)
    mobile = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    pincode = Column(String)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    children = relationship("Children", back_populates="parent")