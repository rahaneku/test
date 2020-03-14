import openpyxl

book = openpyxl.load_workbook('c:\\temp\\test.xlsx')

sheet = book.active

rows = sheet.rows

values = []

for row in rows:
    for cell in row:
        values.append(cell.value)
print(values)
