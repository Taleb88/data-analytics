#a dictionary is a data structure that holds data in the form of
# key:value pairs where each key can hold a single value
#the key values must be immutable
#the supported data types for the keys are int, str, list (array), and tuples
#the keys should be unique and immutable, but the values can be duplicates
students = {'student1': 'Taleb', 'student2':'Moses', 'student3': 'Danny'}
print(students) #key:value pairs printed

#arrays can be stored in dictories as well
foods = {'vegetables':['lettuce', 'potato', 'leek'], 
			'candy': 'hersheys', 'guest': 'johnson'}
print(foods) #key:value pairs printed, including the array

#using a dict() function to convert data types to dictionaries
colors = dict({1: 'red', 2: 'blue', 3: 'brown'}) 
sizes = dict([(1,'large'), (2,'medium'), (3, 'small')]) #list of tuples convered to dictionary
print(sizes) #dictionary printed out
print(colors) #dictionary printed out

#accessing elements in dictionary by key instead of indices
shirts = {1:'xxl', 2:'xl', 3:'l', 4:'m', 5:'s', 'color': 'red', 'store':'smith'}
print(shirts['color']) # red

#updating elements in dictionary
bags = {1: 'louis vitton', 2: 'gucci', 3: 'sears', 4: 'foot locker', 5: 'bentley'}
bags[1] = 'old navy' #replacing first element of array, louis vitton, with old navy
print(bags) #old navy, gucci, sears, foot locker, bentley

#adding elements in dictionary
chairs = {1:'suede',2:'leather',3:'pleather'}
chairs[4] = 'sleek'
print(chairs) #4. 'sleek' added to dictionary

#clearing/removing all items from dictionary with clear() method
math = {1: '1', 2: '2', 3: '3'}
math.clear() #clear all key:value items
print(math) #prints out -> {}

#note - dictionaries support multiple methods such as: 
#	dict.has_key(), dict.items(), dict.keys(),
#	dict.values(), dict.update(), dict.copy(), dict.sorted()