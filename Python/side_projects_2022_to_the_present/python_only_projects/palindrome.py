'''
palindrome - a word that does not change when the letters are reversed
    ex: tat, noon, deed, peep, wow, kayak, repaper, etc...
'''
#palindrome test
y = "dud"[::-1] #using slicing to reverse the string
print(y) #dud

#palindrome test part 2
z = input("Please type in a word: ").lower()

if(z == z[::-1]):
    print("This is a palindrome")
else:
    print("Not a palindrome")