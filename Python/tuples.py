#tuples are ordered collection of objects
#they belong to a sequence data type like lists, but are immutable since
# an assignment operator (=) cannot be used to update the values in them
#they can be accessed, but cannot be modified after they have been declared
food = ('raspberry', 'kiwi', 'mango', 'watermelon')
colors = ('orange', 'yellow', 'burgundy', 'phthalo blue')
numbers = (10, 20, 30, 40, 50)

print(food) #raspberry, kiwi, mango, watermelon
print(food[1]) #kiwi
print(food[2:]) #mango, watermelon
print(food + colors) #concatenates/combines both tuples together
print(numbers * 2) #values of the tuple repeat 2X

#an element in a tuple cannot be updated, but the entire tuple can be removed
del food #removing the "food" tuple with the del keyword
print(food) #NameError thrown since the "food" tuple was deleted

#advantages of tuples over lists
# 1. Speed, faster to iterate through a tuple, thus slightly boosting performance
# 2. Immutable, can be used as keys inside dictionaries
# 3. Store heterogenous data types, compared to lists storing hemogenous data types
# 4. Data can be write-protected