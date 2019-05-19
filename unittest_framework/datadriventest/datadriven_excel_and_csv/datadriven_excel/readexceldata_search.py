import xlrd

def getData():
    workbook=xlrd.open_workbook("SearchScenarioData.xlsx")
    sheet=workbook.sheet_by_index(0)
    data=[]
    for i in range(1,sheet.nrows):
        data.append([sheet.cell_value(i,0),sheet.cell_value(i,1)])

    return data