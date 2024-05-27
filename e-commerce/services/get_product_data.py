from fastapi import HTTPException
from models.Products import Products

def get_product_data(session):
    product_list = session.query(Products).all()
    if not product_list:
        raise HTTPException(
            status_code=404,
            details="Products not found"
        )
    return product_list