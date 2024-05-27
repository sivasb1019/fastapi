from fastapi import HTTPException, status

from models.Products import Products
from utils.password_auth import hash_password

 
def update_products(product_id, request, current_user, db):
    try:
        if current_user.role != 2:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid operation: Adding products are unauthorized for customers and admins."
            )
        product = db.query(Products).filter(Products.product_id == product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "Product not found or invalid id"
            )
        if request.product_name:
            product.product_name = request.product_name
        if request.price:
            product.price = request.price
        if request.count:
            product.count = product.count + request.count
            if product.count < 0:
                product.count = 0
        if request.discount_percentage:
            product.discount_percentage = request.discount_percentage
            discount_price = product.price * (request.discount_percentage/100)
            product.price = product.price - discount_price
            product.offer = True

        db.commit()
    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid operation - Not authenticated"
        )
    return {"message": f"Product updated successfully for id,'{product.product_id}'"}
