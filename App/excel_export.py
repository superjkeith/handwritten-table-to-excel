from openpyxl import Workbook
def export_to_excel(rows, output_path: str):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Table Data"
    for row_index, row in enumerate(rows, start=1):
        for col_index, value in enumerate(row, start=1):
            sheet.cell(row=row_index, column=col_index, value=value)
    workbook.save(output_path)
    