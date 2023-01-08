user = int(input('please enter a number: \n'))

if user % 18 == 0 & user % 11 == 0:
    print("fizzbuzz")
elif user % 6 == 0:
    print("fizz")
elif user % 4 == 0:
    print('buzz')
else:
    print('fail')