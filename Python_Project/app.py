import openpyxl as xl
wb=xl.load_workbook("4A562000.xlsx")
sheet=wb["Sheet2"]
cell=sheet['C10']
#a=sheet.cell(4,3)
for row in range(4,11):
    cell=sheet.cell(row,2)
    print(cell.value)
