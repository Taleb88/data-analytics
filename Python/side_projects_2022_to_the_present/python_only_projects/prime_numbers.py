#print prime numbers between 1 and 50 (advanced)
for x in range(51):
    if x > 1: # number has to be greater than 1
        for y in range(2,x): #loop through the range again with 2 as the starting point
            if x % y == 0: #x/y returns a remainder of 0, break out of the loop
                break
        else:
            print(x) #otherwise, print the numbers
