from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.customer_schemas import Customer_Response, Purchase_Response, Purchase_Request
from schemas.auth_schemas import TokenData
from services.get_product_data import get_product_data
from services.add_cart_products import add_cart_products
from utils.get_current_user import get_current_user
from utils.get_session import get_session

router = APIRouter(prefix="/customer", tags=["customer"])


@router.get("/get_products", response_model=list[Customer_Response])
async def get_products(session: Session = Depends(get_session)):
    return get_product_data(session)

@router.post("/add_to_cart", response_model=Purchase_Response)
async def add_to_cart(request: list[Purchase_Request],
                      current_user: TokenData = Depends(get_current_user),
                      session: Session = Depends(get_session)):
    return add_cart_products(request, current_user, session)
