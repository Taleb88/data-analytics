import openpyxl

wb = openpyxl.load_workbook('file_example_XLS_5000.xlsx')
sheet = wb['Sheet2']

print(tuple(sheet['A1':'F25'])) #A1 through F25
for x in sheet['A1':'F25']:
    for y in x:
        print(y.coordinate,y.value)
    print('=============================')