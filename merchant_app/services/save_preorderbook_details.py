from fastapi.exceptions import HTTPException
from models.PreOrderBook import  PreOrderBook
from utils.get_id import get_id

def save_preorderbook_details(requestList, session1, session2):    
    try:
        for request in requestList:
            session_data = get_id(session2)
            PreOrderBook_instance = session1.query(PreOrderBook).filter(PreOrderBook.Id == request.id).first()
            if PreOrderBook_instance:
                PreOrderBook_instance.UPI = request.upi,
                PreOrderBook_instance.UPI_Type = request.upi_type,
                PreOrderBook_instance.UPI_Trans_No = request.upi_trans_no,
                PreOrderBook_instance.UPI_Amount = request.upi_amount,
                PreOrderBook_instance.Amount = request.amount,
                PreOrderBook_instance.Receipt_No = request.receipt_no
                PreOrderBook_instance.Payment_Type = request.payment_type
                PreOrderBook_instance.Customer_Type = request.customer_type
                PreOrderBook_instance.Date = request.date

            else:
                PreOrderBook_instance = PreOrderBook(
                    Customer_Name = request.customer_name,
                    Phone_No = request.phone_no,
                    Receipt_No = request.receipt_no,
                    Payment_Type = request.payment_type,
                    Amount = request.amount,
                    Status = request.status,
                    Customer_Type = request.customer_type,
                    Date = request.date,
                    Branch_Id = session_data.get("branch_id"),
                    Merchant_Id = session_data.get("merchant_id")
                )
            session1.add(PreOrderBook_instance)
            session1.commit()
            session1.refresh(PreOrderBook_instance)
            session1.close()

        return {"message": "Pre-Order details added succesfully."}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))