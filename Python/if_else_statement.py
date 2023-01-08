x = int(input("what is 10 x 10?: ")) #typecast string into integer data type

if x == 100:
	print(True)
else:
	print(False)

y = str(input("who is the father?: ")) #typecast string into string data type

if y == "Taleb":
	print(True)
else:
	print(False)

z = int((input("please input a number: ")))

if z % 2 == 0: #if there is no remainder.....
	print("Even")
else:
	print("Odd")
