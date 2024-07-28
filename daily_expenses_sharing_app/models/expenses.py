from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.orm_setup import Base

class Expense(Base):
    __tablename__ = 'expenses'

    expense_id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True, nullable=False)
    amount = Column(Float, nullable=False)
    split_method = Column(String, nullable=False)  # equal, exact, percentage
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(Date, default=datetime.utcnow)

    owner = relationship("User", back_populates="expenses")
    splits = relationship("Split", back_populates="expense")

class Split(Base):
    __tablename__ = 'splits'

    split_id = Column(Integer, primary_key=True, index=True)
    percentage = Column(Float, nullable=True)
    exact_amount = Column(Float, nullable=True)
    expense_id = Column(Integer, ForeignKey('expenses.expense_id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_by = Column(Integer, nullable=False, default=1)
    

    expense = relationship("Expense", back_populates="splits")
    user = relationship("User")