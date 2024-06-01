from utils.get_branch import get_branch

def create_excel( writer, book_type, branch_id, duration_str, title, header_color, header_text_color, opening_balance_value, df, session):
    workbook = writer.book
    header_format = workbook.add_format({'bg_color': header_color,'color': header_text_color, 'bold': True, 'align': 'center'})
    worksheet = workbook.add_worksheet(book_type)
    title_format = workbook.add_format({'bold': True})
    worksheet.merge_range('A1:I1', f"Advance Auto Parts - {get_branch(branch_id, session)}")

    worksheet.merge_range('A2:I2', title, title_format) 

    worksheet.merge_range('A3:I3', duration_str)

    for idx, col in enumerate(df.columns):
        worksheet.set_column(idx, idx, 17)

    for col_num, value in enumerate(df.columns): 
        header_text = value.replace("_", " ").upper()
        worksheet.write(3, col_num, header_text, header_format)

    start_row = 6 if book_type == 'ExpenseFund' else 7        
    if book_type == 'DailyLog':
        col_names = ['Amount', 'PreOrder_Receipt_Amount', 'Pending_Balance']  
                    # worksheet.write(6,0,"Date Here")
        worksheet.write(6, 1, "Opening Balance") 
        cash_amount_col_index = df.columns.get_loc('Amount')
        worksheet.write(6, cash_amount_col_index, opening_balance_value)     

        opening_balance_float = float(opening_balance_value)

        for col_name in col_names:
            col_sum = df[col_name].sum() + opening_balance_float if col_name == 'Amount' else df[col_name].sum()
            col_idx = df.columns.get_loc(col_name)
            sum_format = workbook.add_format({'bold': True, 'color': 'red'})
            worksheet.write(4, col_idx, col_sum, sum_format)

    elif book_type == 'ExpenseFund':
        col_names = ['Amount']
        col_sum = df['Amount'].sum()
        col_idx = df.columns.get_loc('Amount')
        sum_format = workbook.add_format({'bold': True, 'color': 'red'})
        worksheet.write(4, col_idx, col_sum, sum_format)

                        
    df.to_excel(writer, sheet_name=book_type, index=False, startrow=start_row, header=False)


