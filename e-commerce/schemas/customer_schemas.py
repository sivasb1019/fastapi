from pydantic import BaseModel


class Purchase_Request(BaseModel):
    product_id: int
    count: int

class Product_Response(Purchase_Request):
    product_name: str
    price: float

class Customer_Response(Product_Response):
    customer_name: str
    customer_id: int

class Purchase_Response(BaseModel):
    purchased_id: int
    product: list[Product_Response]
    




    