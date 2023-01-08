#write() method used to write into a file
with open('write.txt', 'w') as file_obj:
	#check to see if file is closed
	print(file_obj.closed)
	#write into file
	file_obj.write('I love coding in Python')

with open('write.txt', 'r') as obj:
	#read the file
	print(obj.read())

print('file closed = ',obj.closed) #check to see if the file is closed