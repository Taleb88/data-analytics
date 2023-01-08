#read() function allows the program to read a file
with open('nantucket_poem.txt') as file_obj:
	#checking if the file is closed
	print(file_obj.closed)

with open('nantucket_poem.txt') as obj:
	print(obj.read())

print("file closed = ", obj.closed) #checking if the file is closed

#note - readlines() method used to return list of all possible lines in a file