from fastapi import HTTPException, status

from models.Products import Products
from models.AddToCart import AddToCart
from schemas.customer_schemas import Product_Response
from schemas.customer_schemas import Purchase_Response
from utils.get_user import get_user
 
def add_cart_products(request_list, current_user, db):
    
    if current_user.role != 3:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid operation: Adding products are unauthorized for sellers and admins."
        )
    user = get_user(current_user.email, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials."
        )
    product_list = []
    for request in request_list:
        product = db.query(Products).filter(Products.product_id == request.product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= f"Given product id '{request.product_id}' not found"
            )
        if product.count < request.count:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail= f"Given count exceeds the product count"
            )
        product.count = product.count - request.count
        product_price = product.price * request.count
        try:
            new_product = AddToCart(
                customer_id = user.user_id,
                product_name = product.product_name,
                price = product_price,
                product_id = product.product_id,
                product_count = request.count
            )
            db.add(new_product)
            db.commit()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
                )
        
        product_list.append(Product_Response(product_id=new_product.product_id,
                                             count=new_product.product_count,
                                             price=new_product.price,
                                             product_name=new_product.product_name))
    
    return Purchase_Response(purchased_id=new_product.purchased_id, product=product_list)

