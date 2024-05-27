from sqlalchemy import Column, String, Float, Integer, Boolean, TIMESTAMP, func
from databases.db_setup import Base

class Products(Base):
    __tablename__ = "products_table"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    offer = Column(Boolean, nullable=False)
    discount_percentage = Column(Float)
    count = Column(Integer)
    added_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())