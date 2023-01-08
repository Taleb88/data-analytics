#inheritance consists of a child (derived) class inheriting properties from a
# parent (base) class
#the child class possess an 'IS A' property with its base class

class Car:
	#properties
	def wheels(self):
		print('The vehicle has 4 wheels.')
	def color(self):
		print('The vehicle is black.')

class Mercedes(Car): #inherit properies from Car class
	def price(self):
		print('The price of a Mercedes is $40,000')

class Peugeot(Car): #inherit properies from Car class
	def warranty(self):
		print('A Peugeot comes with a 10-year warranty.')

#lets inherit traits from the Car class
m = Mercedes()
m.wheels()
m.color()
m.price()

print('=========================')

p = Peugeot()
p.wheels()
p.color()
p.warranty()

''' types of inheritance:
		single-level: base class only has 1 derived class
		multi-level: base class has multiple derived classes
		multiple: multiple base classes have 1 derived class that 
					inherits all of the properities from the base
					classes
		hierarchical: base class having multiple child/derived 
						classes
'''