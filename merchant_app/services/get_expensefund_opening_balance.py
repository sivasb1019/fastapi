from fastapi import HTTPException
from sqlalchemy import text
from utils.get_id import get_id

def get_expensefund_opening_balance(input_date, session1, session2):
    try:
        session_data = get_id(session2)
        ob_instance = session1.execute(text("call expensefund_opening_balance(:input_date, :branch_id, :merchant_id)"),
                {"input_date": input_date, "branch_id": session_data.get("branch_id"), "merchant_id": session_data.get("merchant_id")})
        opening_balance = ob_instance.fetchone()[0]
        return {
            "opening_balance": opening_balance
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))