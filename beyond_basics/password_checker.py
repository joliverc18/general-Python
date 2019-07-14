correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")
while password != correct_password:
    print("Invalid password!")
    password = input("Enter password:")

#String formatting v1 (Recommended way of doing)
message = "Hi %s %s you have logged in" % (name, surname)
print(message)

#String formatting v2 (Not recommended, doesn't work)
message = "Hi", name, surname, "you have logged in"
print(message)
