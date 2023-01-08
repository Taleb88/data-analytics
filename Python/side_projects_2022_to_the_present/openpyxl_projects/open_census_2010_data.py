# arrange population and number of census tracts for each county
import openpyxl, pprint

print('Opening the workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# we must fill in county data with each country's population and tracts
print('Reading the rows...')
for row in range(2, sheet.max_row + 1):
    # each row in spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    population = sheet['D' + str(row)].value
#open a new text file and write contents of count_data to it
county_data.setdefault(state,{})
#make sure the key for this state exists
county_data[state].setdefault(county, {'tracts':0, 'population':0})
#each row represents one census tract, let's increment by one
county_data[state][county]['tracts'] += 1
#let's increase county population by the population in this census tract
county_data[state][county]['population'] += int(population)
#open new text file and write contents of county_data to it
print('Writing confidential census data results...')
data_results_file = open('census_2010.py','w')
data_results_file.write('All Census Data  = ' + pprint.pformat(county_data))
data_results_file.close()
print('Finished')