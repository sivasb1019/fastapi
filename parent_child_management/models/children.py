from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database.orm_setup import Base

# Define the Children model, which represents a child associated with a parent
class Children(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    dob = Column(Date, nullable=False)
    parent_id = Column(Integer, ForeignKey('parents.id'), nullable=False)
    created_at = Column(Date, default=datetime.utcnow)
    updated_at = Column(Date, default=func.now(), onupdate=func.now())
    parent = relationship("Parent", back_populates="children")