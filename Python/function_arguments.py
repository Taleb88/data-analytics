#default argument - not passing a value into an argument in a function
def car(color, size="large"):
	print(color)
	print(size)

car(color="red")

#required argument - few arguments must be passed while making a call to a function
# when it is called, the number of arguments must match the number in the declaration
def house(neighborhood,windows,oven,rooms):
	print("neighborhood:",neighborhood)
	print("windows:",windows)
	print("oven:",oven)
	print("rooms:",rooms)

house("bronxville","stained glass","magic chef",4)

#keyword arguments - when we do not want to remember the order of arguments
#it remembers the argument values by the keyword given during the
# declaration of the function
def office(neighborhood,windows,desks,bathrooms):
	print("neighborhood:",neighborhood)
	print("windows:",windows)
	print("desks:",desks)
	print("bathrooms:",bathrooms)

office(windows="glass",neighborhood="chelsea",bathrooms=4,desks=25)

#variable-length argument - used when we do not know number of arguments
# required in an object when defining a function following the syntax *args
def person(*args):
	for x in args:
		print(x)

person('Taleb','Data Analyst','Male',34)