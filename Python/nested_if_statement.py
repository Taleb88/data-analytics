x = str(input("what is my favorite color?: "))
#nested if statements are useful for making a decision off a preexisting condition
if (x == "red"):
	print("correct") #if answer == "red", move on to the next if statement within the if parent block
	
	x = str(input("what is my favorite season?: "))
	if (x == "summer"):
		print("correct")

print("finished")