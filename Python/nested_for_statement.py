animal = ["python", "alligator", "dog", "cat", "gorilla", "panda"]
size = ["big"]

category = [1] # category = [1, 2, 3, 4, 5] (prints same sentence 5X) 

for x in category:
	for y in size:
		for z in animal:
			print(x, y, z)
