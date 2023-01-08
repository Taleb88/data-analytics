# adding to array and printing out results without having to use multiple print/input statements
dog_names = []

while True:
    print('enter name of dog' + str(len(dog_names) + 1) + ' or press enter key only to exit')
    name = input()
    if name == '':
        break
    #let's add the names to the array
    dog_names += [name] #list concatenation
    print("List of dog names:")
    #lets iterate through the dog_names array to print out the list of dog names
    for name in dog_names:
        print(" ", name)