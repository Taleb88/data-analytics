import random

def game(answer):
    if answer == 1:
        return 'It is certain.' #using a return keyword to return value or expression the function should return
    elif answer == 2:
        return 'It is decidedly so.'
    elif answer == 3:
        return 'As I see it, yes.'
    elif answer == 4:
        return 'Most likely.'
    elif answer == 5:
        return 'Reply hazy, try again.'
    elif answer == 6:
        return 'Concentrate and ask again.'
    elif answer == 7:
        return 'My sources say no.'
    elif answer == 8:
        return 'Outlook not so good'

r = random.randint(1, 9)
result = game(r)
print(result)