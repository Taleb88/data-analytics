import random
y = random.randint(1,10) #value has to be between 1 and 10

for x in range(1, 4): # user has 3 guesses
    print("guess a number between 1-10: ")
    guess = int(input())

    if guess == y:
        print(f"{y} is the correct answer. you win. took {x} attempts")
        break
    elif guess > y:
        print("too high")
    elif guess < y:
        print("too low")
    else:
        break;