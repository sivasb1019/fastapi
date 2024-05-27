from fastapi import HTTPException, status

from models.Products import Products
from schemas.products_schemas import Product_Response
 
def add_products(request_list, current_user, db):
    
    if current_user.role != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid operation: Adding products are unauthorized for customers and admins."
        )
    product_list = []
    for request in request_list:
        product = db.query(Products).filter(Products.product_name == request.product_name).first()
        if product:
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail= f"Given product '{request.product_name}' already exist"
            )
        if request.discount_percentage:
            discount_price = request.price * (request.discount_percentage/100)
            request.price = request.price - discount_price
            request.offer = True
        try:
            new_product = Products(**request.dict())
            db.add(new_product)
            db.commit()
        except:
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=f"Given product '{request.product_name}' already exist"
                )
        
        product_list.append(Product_Response(product_id=new_product.product_id, product_name=new_product.product_name))

    return product_list
