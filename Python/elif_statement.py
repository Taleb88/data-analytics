#grades
# > 89 = A
# > 79 = B
# > 69 = C
# > 59 = D
# < 58 = F

x = int(input("please enter your grade: "))

if (x >= 90):
	print("A")
elif(x >= 80):
	print("B")
elif(x >= 70):
	print("C")
elif(x >= 60):
	print("D")
elif(x < 60):
	print("F")