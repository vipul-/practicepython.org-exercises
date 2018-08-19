import datetime
now = datetime.datetime.now()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
yearAt100 = (100-age)+now.year

print("You will be 100 years old in " + str(yearAt100))