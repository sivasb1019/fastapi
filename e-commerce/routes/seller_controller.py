from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.products_schemas import Add_Product, Update_Product, Product_Response
from schemas.auth_schemas import TokenData
from services.add_products import add_products
from services.update_products import update_products
from utils.get_current_user import get_current_user
from utils.get_session import get_session

router = APIRouter(prefix="/seller", tags=["seller"])

@router.post("/create_product", response_model=list[Product_Response])
async def create_product(request: list[Add_Product],
                         current_user: TokenData = Depends(get_current_user),
                         session: Session = Depends(get_session)):
    return add_products(request, current_user, session)

@router.put("/update_product")
async def update_product(product_id: int,
                         request: Update_Product, 
                         current_user: TokenData = Depends(get_current_user),
                         session: Session = Depends(get_session)):
    return update_products(product_id, request, current_user, session)