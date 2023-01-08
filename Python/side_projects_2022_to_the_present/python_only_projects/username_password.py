#we want to validate a username and password
username = input("enter your username: ").lower()

if(username == "Taleb".lower()):
    print("++++++++++++++++++")
    password = input("enter your password: ")
    if(password == "Knicks"):
        print("access granted")
    else:
        print("access Denied")
else:
    print("access denied")