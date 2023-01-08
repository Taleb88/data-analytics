#functions are blocks of resuable code that can be executed from 
# anywhere in a program
#Two types of functions - Built-in and User-defined
#def keyword used to define/declare a function
def hello_world():
	x = str(input("Please say Hello World: "))

	if(x == "Hello World"):
		print("Thanks :)")
	else:
		print("Fail")

hello_world() #calling out the function after declaration

#if we want to return any statement, writing the "return" statement is required
def math_problem(x):
	
	if(x >= 15):
		return "Great"
	else:
		return "No bueno"

print(math_problem(15)) #Great

