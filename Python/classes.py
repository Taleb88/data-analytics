#classes are data strutures that are the blue prints from which objects are created
#classes are used to bundle data and their functionalities
#classes have a set of attributes (variables) and methods (functions) attached 
# to them
#objects are instances of a class, resembling real-world entities
#a single class can have many objects
#objects access attributes of a class with dot "." operator
#"self" keyword - first parameter passed inside every method
# used to access attributes and methods of each object
#a method that takes no argument still must have a pass keyword as an
# argument explicity in that method
#__init__ - special method working as a class constructor
# automatically gets invoked as soon as any object of that class is 
#  instantiated (in use)
# initializes all variables associated within an object

class Employees:
	'''class named Employees is created'''

	#class attributes
	employee_division = "Information Technology(IT)" # defined publicly for global access
	#instance attribute acting as a constructor
	def __init__(self, name, salary, role):
		self.name = name
		self.salary = salary
		self.role = role

	def has_bonus(self):
		print('This employee qualifies for a bonus.')

	def office_space(self):
		print("This employee's cubicle is 80 sq ft.")
#creating a new object of Employees class and passing instance attributes
Employee1 = Employees('Taleb',50000,'Data Analyst')

#acccesing class variable/attribute using dot (.) operator
print(Employee1.employee_division)

#accessing instance attributes using dot (.) operator
print('The name of the employee is: ',Employee1.name)
print('The salary of the employee is: ',Employee1.salary)
print('The role of the employee is: ',Employee1.role)

#accessing class member functions using dot (.) operator
Employee1.has_bonus()
Employee1.office_space()