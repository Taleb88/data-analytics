number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in number:
	print(x)
	x += 1 # exclusive to int values

	if x == 6:
		break; #breaks out of the loop when we reach 6, thus omitting 6-10

print("finished")

animal = ["bear","frog","turtle","fish"]

for x in animal:
	print(x)

	if x == "bear":
		print("executed inside if block statement")
		continue #continue transvering the list
		print("continue")

print("finished")

toys = ["car", "ball", "doll", "plane", "bike"]

for x in toys:
	pass #null operator that breaks out of loop without an error thrown

print("finished")