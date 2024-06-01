from fastapi import HTTPException
from models.DailyLog import DailyLog
from utils.get_id import get_id

def save_dailylog_details(requestList, session1, session2):
    try:
        for request in requestList:
            session_data = get_id(session2)
            DailyLog_instance = DailyLog(
                Sales_Type = request.sales_type,
                Sales_Code = request.sales_code,
                Date = request.date,
                Bill_No = request.bill_no,
                Customer_Type = request.customer_type,
                Bill_Value = request.bill_value,
                Amount = request.amount,
                PreOrder_Receipt_No = request.advance_receipt_no,
                PreOrder_Customer_Name = request.advance_customer_name,
                PreOrder_Receipt_Amount = request.advance_receipt_amount,
                Pending_Balance = request.pending_balance,
                Branch_Id = session_data.get("branch_id"),
                Merchant_Id = session_data.get("merchant_id")
            )

            session1.add(DailyLog_instance)
            session1.commit()
            session1.refresh(DailyLog_instance)
            session1.close()
        return {"message": "DailyLog details added successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
