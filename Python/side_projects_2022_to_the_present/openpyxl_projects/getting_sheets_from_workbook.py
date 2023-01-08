import openpyxl

wb = openpyxl.load_workbook('financial_sample.xlsx')

print(wb.sheetnames) #['Sheet1', 'Sheet2', 'Sheet3']

sheet = wb['Sheet3']

print(sheet) #<Worksheet "Sheet3"
print(type(sheet)) #<class 'openpyxl.worksheet.worksheet.Worksheet'>
print(sheet.title) #'Sheet 3'

another_sheet = wb.active #let's see what the active sheet is
print(another_sheet)