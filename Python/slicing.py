#slicing used to return range of elements from a list
#basic syntax -> [start:stop] 
#complex syntax -> [start:stop:step]
#colon is the slicing operator
#start value inclusive to range, stop value exclusive to range if filled in

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(elements[:6]) #1, 2, 3, 4, 5, 6
print(elements[4:]) #5, 6, 7, 8, 9, 10
print(elements[1:5]) #2, 3, 4, 5
print(elements[7:9]) #8, 9

colors = ["black", "white", "brown", "orange", "purple", "violet", 
			"red", "maroon"]

print(colors[0:3:2]) #black, brown (every 2nd element of array gets skipped)
print(colors[3:4:3]) #orange
print(colors[1:5:2]) #white, orange
print(colors[::7]) #black, maroon
print(colors[0::6]) #black, red