import openpyxl

wb = openpyxl.load_workbook('file_example_XLS_5000.xlsx')
sheet = wb['Sheet3']

print(tuple(sheet['B1':'J50'])) #B1 through J50
# nested for loop to iterate around spreadsheet and print out data from B1 through J50
for x in sheet['B1':'J50']:
    for y in x:
        print(y.coordinate,y.value) #print the cordinates and values from B1 through J50
    print('===========================') #separate data per row for readability purposes