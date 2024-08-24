def signin(username,password):

    myfile = open("stored.txt", "r")
    uname = myfile.readline().strip()
    pword = myfile.readline().strip()
    myfile.close()
    if(username == uname and password == pword):
        return True
    else:
        return False

uname = input("Enter your UserName: ")
pword = input("Enter your Password: ")

if(signin(uname,pword) == True):
    print("Successfull Login")
else:
    if not signin(uname,pword):
        print("Your Login is Failed")
        exit()