import xlrd

def getdata():
    wb=xlrd.open_workbook("PayeeDetails.xlsx")
    sheet=wb.sheet_by_name("PayeeDetails")

    data=[]
    for i in range(1,sheet.nrows):
        li=[]
        for j in range(sheet.ncols):
            li.append(sheet.cell_value(i,j))
        data.append(li)
    return(data)

