from fastapi.exceptions import HTTPException
from models.PreOrderBook import  PreOrderBook
from utils.get_id import get_id

def verify_receipt_number(PreOrder_Receipt_No, session1, session2):
    try:
        session_data = get_id(session2)
        receipt = session1.query(PreOrderBook).filter(PreOrderBook.Receipt_No == PreOrder_Receipt_No, 
                                                      PreOrderBook.Branch_Id == session_data.get("branch_id"),
                                                      PreOrderBook.Merchant_Id == session_data.get("merchant_id")).first()
        if not receipt:
            raise HTTPException(status_code=400, detail="PreOrder receipt number is invalid")
        
        return receipt
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
