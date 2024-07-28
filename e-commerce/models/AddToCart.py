from sqlalchemy import Column, String, Float, Integer, Boolean, TIMESTAMP, func
from databases.db_setup import Base

class AddToCart(Base):
    __tablename__ = "add_to_cart"

    
    purchased_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    product_id = Column(Integer, nullable=False)
    product_count = Column(Integer, nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), server_default=func.now())