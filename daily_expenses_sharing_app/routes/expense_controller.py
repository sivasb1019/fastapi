# from datetime import date


from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from typing import Literal

from database.orm_setup import get_session
from schemas.expense_schema import CreateExpense, ExpenseList
from utils.get_current_user import get_current_user
from services.create_expenses_details import create_expenses_details
from services.view_user_expenses_detail import view_user_expenses_detail
from services.view_overall_expenses_detail import view_overall_expenses_detail
from services.download_balance_sheet import download_balance_sheet

router = APIRouter(prefix="/expenses")


@router.post("/create-expenses", tags=["expense"])
async def create_expenses(request: CreateExpense, background_tasks: BackgroundTasks,
                           current_user: object = Depends(get_current_user), session: Session = Depends(get_session)):
    return create_expenses_details(request, background_tasks, current_user, session)

@router.get("/view-user-expenses", tags=["expense"], response_model=list[ExpenseList])
async def view_user_expenses(current_user: object = Depends(get_current_user), session: Session = Depends(get_session)):
    return view_user_expenses_detail(current_user, session)

@router.get("/view-overall-expenses", tags=["expense"], response_model=list[ExpenseList])
async def view_overall_expenses(current_user: object = Depends(get_current_user), session: Session = Depends(get_session)):
    return view_overall_expenses_detail(current_user, session)

@router.get("/download-balancesheet", tags=["expense"])
async def download_balancesheet(request: Literal["Individual Expenses", "Overall Expenses", "Both"], current_user: object = Depends(get_current_user), session: Session = Depends(get_session)):
    return download_balance_sheet(request, current_user, session)


