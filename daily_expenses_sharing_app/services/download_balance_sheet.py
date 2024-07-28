import pandas as pd
from io import BytesIO
from fastapi import Response, HTTPException

from services.view_user_expenses_detail import view_user_expenses_detail
from services.view_overall_expenses_detail import view_overall_expenses_detail

def download_balance_sheet(request, current_user, db):
    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        if request == "Individual Expenses":
            expenses = view_user_expenses_detail(current_user, db)
            create_excel(request, writer, expenses)
            
        elif request == "Overall Expenses":
            expenses = view_overall_expenses_detail(current_user, db)
            create_excel(request, writer, expenses)
        
        elif request == "Both":
            create_excel("Individual Expenses", writer, view_user_expenses_detail(current_user, db))
            create_excel("Overall Expenses", writer, view_overall_expenses_detail(current_user, db))

            

    
    # Return the Excel file as a response
    return Response(
        excel_file.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=balance_sheet.xlsx"
        }
    )


def create_excel(sheet_name, writer, expenses):
    expense_columns = ["expense_id", "description", "amount", "split_method", "created_at"]
    split_columns = ["split_id", "percentage", "exact_amount", "user_id", "created_by"]

    # Prepare a list to hold the flattened data
    expense_data = []

    # Iterate over each expense
    for expense in expenses:
        # For each expense, iterate over its splits
        for split in expense.splits:
            # Create a dictionary for the current row
            row_dict = {column: getattr(split, column) for column in split_columns}
            # Add split details to the row
            row_dict.update({column: getattr(expense, column) for column in expense_columns})
            # Append the row dictionary to the expense_data list
            expense_data.append(row_dict)

    # Create a DataFrame from the flattened data
    df = pd.DataFrame(expense_data)
    # Set null values to 0 for percentage and exact_amount columns
    df['percentage'] = df['percentage'].fillna(0)
    df['exact_amount'] = df['exact_amount'].fillna(0)

    # Write the DataFrame to an Excel file
    title = sheet_name
    header_color = '#228B22'
    header_text_color = "#FFFFFF"
    workbook = writer.book
    header_format = workbook.add_format({'bg_color': header_color,'color': header_text_color, 
                        'bold': True, 'align': 'center'})

    worksheet = workbook.add_worksheet(title)
    for idx, col in enumerate(df.columns):
        worksheet.set_column(idx, idx, 17)

    for col_num, value in enumerate(df.columns): 
        header_text = value.replace("_", " ").upper()
        worksheet.write(0, col_num, header_text, header_format)

    for idx, col in enumerate(df.columns):
        worksheet.set_column(idx, idx, 17)

    df.to_excel(writer, index=False, startrow=2, sheet_name=sheet_name, header=False)
