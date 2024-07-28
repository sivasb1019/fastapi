from datetime import datetime, timedelta

def get_day(history_type):
    if history_type == 1:
        return datetime.now().date()
    
    elif history_type == 2:
        return datetime.now().date() - timedelta(days=1)
         
    elif history_type == 3:
        return datetime.now().date() - timedelta(days=7)
    
    elif history_type == 4:
        return datetime.now().date() - timedelta(days=31)
    
    elif history_type == 5:
        return datetime.now().date() - timedelta(days=365)