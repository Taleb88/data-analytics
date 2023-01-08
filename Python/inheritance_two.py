class House:
	def price(self):
		print('The property is $250,000')
	def location(self):
		print('It is located in Mount Vernon, NY')
	def timezone(self):
		print('Is in the Eastern Standard Timezone')

class Door(House): #object of the derived class, House
	def color(self):
		print('The color of the doors is brown.')
	def size(self):
		print('The size of the doors is big.')

h = House()
h.price()
h.location()
h.timezone()

print('+++++++++++++++++++++++++++++++')

d = Door()
d.price()
d.location()
d.timezone()
d.color()
d.size()