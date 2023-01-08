''' to open a file -> 
open(name of file [, access_mode][,buffer value])
access_mode parameter is optional
'''
#closing a file
file_obj = open('test.txt','r') #r -> read the file

print(file_obj.name) #name of the file
print(file_obj.mode) #name of the mode the file is in -> r

file_obj.close() #closing the file
print('file is now closed',file_obj.closed) #evaluates to True since file is now closed

'''
using the "with statement" to guarantee close() method gets automatically 
 executed as we move out of the with statement block	
'''
with open('random.txt','r') as file_obj:
	print(file_obj.name)

print("file closed?",file_obj.closed) #evaluates to true
