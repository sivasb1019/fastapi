from pydantic import BaseModel


class Add_Discount(BaseModel):
    discount_percentage: float | None = None

class Add_Product(Add_Discount):
    product_name: str 
    price: float
    offer: bool = False
    count: int

class Update_Product(Add_Discount):
    product_name: str | None = None
    price: float | None = None
    offer: bool | None = False
    count: int | None = None

class Product_Response(BaseModel):
    product_id: int
    product_name: str

    