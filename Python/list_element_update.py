#updating elements in lists since lists are mutable
#lists are non-hemogenous, can store multiple data types
cars = ["mercedes", "honda", "toyota"] #pre-declared list

cars[2] = "hundai" #replaces toyota with hundai in the list

print(cars) #mercedes, honda, hundai

#add element to list by using .append() method
buildings = ["hospital", "asylum", "theater", "residental"]
buildings.append("arena") #add arena to list

print(buildings) #hospital, asylum, theater, residental, arena

#insert element into list at a specific location by using .insert() method
groceries = ["fruits", "breads", "poultry", "beef"]
groceries.insert(2, "vegetables") #insert vegetables into 2nd index of list

print(groceries) #fruits, breads, vegetables, poultry, beef

#add multiple elements to list by using .extend() method
animals = ["duck", "goose", "crocodile", "lion", "monkey", "zebra"]
animals.extend(["giraffe", "dinosaur", "shark", "tiger", "wolf"]) #adding elements to pre-declared list

print(animals) #duck, goose, crocodile, lion, monkey, zebra, giraffe, dinosaur, shark, tiger, wolf

#popping element from list using .pop() method (does not require an argument, but can be used)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers.pop() #removing 8 from list 

print(numbers) #1, 2, 3, 4, 5, 6, 7

#deleting element from list using .remove() method (requires an argument)
names = ["Taleb", "Matthew", "Moses", "Jaime"]
names.remove("Jaime") #delete Jaime from list

print(names) # Taleb, Matthew, Moses

#using del[] keyword to delete elements inside list
streets = ["main", "water", "fulton", "duane", "reade"]
del streets[3]; #delete duane from list

print(streets) #main, water, fulton, reade