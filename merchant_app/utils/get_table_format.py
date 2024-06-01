from datetime import datetime
import pandas as pd
from fastapi import HTTPException
from utils.get_common_openingbalance import get_common_openingbalance
from utils.get_expensefund_openingbalance import get_expensefund_openingbalance
from utils.get_booktype_data import get_booktype_data

def get_table_format(book_type, branch_id, Model, duration, history_type, start_date, end_date, session1, session2):
    data = get_booktype_data(Model, branch_id, history_type, start_date, end_date, session1, session2)

    if not data:
        raise HTTPException(status_code=404, detail="No data found in the table")

    if history_type:
        date_duration = duration if history_type < 3 else datetime.now().date()
        duration_str = f"From Date: {duration}; To Date: {date_duration}"
    else:
        duration_str = f"From Date: {start_date}; To Date: {end_date}"
        date_duration = end_date

    if book_type == 'PreOrderBook':
        title = "PreOrder Payments Report"
        header_color = "#FFFF00"
        header_text_color = "#000000"
        include_columns = ['Date', 'Receipt_No', 'Customer_Name', 'Phone_No', 'Amount', 'Status']
        session_data = get_common_openingbalance(date_duration, session1, session2)


    elif book_type == 'DailyLog':
        title = "Daily Log Report"
        header_color = '#228B22'
        header_text_color = "#FFFFFF"
        include_columns = ['Date', 'Bill_No', 'Bill_Value', 'Amount', 'PreOrder_Receipt_No', 
                            'PreOrder_Receipt_Amount', 'Pending_Balance']
        session_data = get_common_openingbalance(date_duration, session1, session2)

    elif book_type == 'AccountCredit':
        title = "Account Credit Report"
        header_color = '#228B22'
        header_text_color = "#FFFFFF"
        include_columns = ['Date', 'Type', 'Deposit_Mode', 'Reason', 'PreOrder_Receipt_No', 'Amount', 'Remaining_Amount']
        session_data = get_common_openingbalance(date_duration, session1, session2)

    elif book_type == 'ExpenseFund':
        title = "Expense Fund Report"
        header_color = '#228B22'
        header_text_color = "#FFFFFF"
        include_columns = ['Date', 'Expense_Fund_Details', 'Amount', 'Balance']
        session_data = get_expensefund_openingbalance(date_duration, session1, session2) 

    opening_balance_value = session_data.get("opening_balance")

    column_names = [column.key for column in Model.__table__.columns if column.key in include_columns]

    df = pd.DataFrame([{column: getattr(row, column) for column in column_names} for row in data])

    
    return duration_str, title, header_color, header_text_color, opening_balance_value, df