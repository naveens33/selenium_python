import xlrd

def getData():
    data=[]
    wb = xlrd.open_workbook("Credential.xlsx")
    sheet = wb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        data.append((sheet.cell_value(i, 0),sheet.cell_value(i, 1)))

    return data
