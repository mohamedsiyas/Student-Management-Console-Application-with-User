from authentication import signin

file = open("students.txt", "a")

i = 0
while i < 3:
    studentid = input("Enter your ID: ")
    studentname = input("Enter your Name: ")
    studentage = input("Enter your Age: ")
    studentlocation = input("Enter your Location: ")


    userdata = "\t          " + studentid + "\t                    " + studentname + "\t          " + studentage + "\t                    " + studentlocation
    file.write(userdata + "\n")

    i = i + 1

    print("thank you for details............")

