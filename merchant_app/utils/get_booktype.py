from models.PreOrderBook import PreOrderBook
from models.DailyLog import DailyLog
from models.AccountCredit import AccountCredit
from models.ExpenseFund import ExpenseFund

def get_booktype(book_type):
    if book_type == "PreOrderBook":
        return PreOrderBook
            
    if book_type == "DailyLog":
        return DailyLog
        
    if book_type == "AccountCredit":
        return AccountCredit
        
    if book_type == "ExpenseFund":
        return ExpenseFund
    
    return ["PreOrderBook", "DailyLog", "AccountCredit", "ExpenseFund"]
    