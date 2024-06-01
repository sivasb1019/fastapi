from fastapi import Response

from utils.get_booktype import get_booktype
from utils.get_day import get_day
from utils.get_table_format import get_table_format
from utils.create_excel import create_excel
import pandas as pd
from io import BytesIO

def downloadbooks(book_type, branch_id, history_type, start_date, end_date, session1, session2):
    Model = get_booktype(book_type)
    duration = get_day(history_type)
    excel_file = BytesIO()
        
    if book_type == "ALL":
        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:    
            for book_type in Model:
                Book_Model = get_booktype(book_type)
                duration_str, title, header_color, header_text_color, opening_balance_value, df = get_table_format(book_type, branch_id, Book_Model, duration, history_type, start_date, end_date, session1, session2)

                create_excel(writer, book_type, branch_id, duration_str, title, header_color, header_text_color, opening_balance_value, df, session2)

        headers = {"Content-Disposition": f"attachment; filename=AllBooks.xlsx"}

    else:
        duration_str, title, header_color, header_text_color, opening_balance_value, df = get_table_format(book_type, branch_id, Model, duration, history_type, start_date, end_date, session1, session2)

        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:    
            create_excel(writer, book_type, branch_id, duration_str, title, header_color, header_text_color, opening_balance_value, df, session2)
        
        headers = {"Content-Disposition": f"attachment; filename={book_type}.xlsx"}

    excel_file.seek(0) 
    return Response(content=excel_file.getvalue(),
                    media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    headers=headers)