import openpyxl

wb = openpyxl.load_workbook('file_example_XLS_5000.xlsx')
sheet = wb['Sheet1']

print(tuple(sheet['A1':'G30'])) #get all cells from A1 to G30
for row_of_cell_objects in sheet['A1':'G30']:
    for cell_object in row_of_cell_objects:
        print(cell_object.coordinate,cell_object.value) #get the coordinate and value
    print('++++++++++++++++++++++++++++++++++') #separates the rows for readability purposes
