import random

rand = random.randint(1, 9)

usr = int(input("Enter a number between 1 and 9: "))

if usr < rand:
    print("Too low")
elif usr > rand:
    print("Too high")
else:
    print("Exactly right") 