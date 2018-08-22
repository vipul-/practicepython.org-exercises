string = input("Enter a long string containing multiple words: ")

stringArray = string.split()
reverse = " ".join(stringArray[::-1])

print(reverse)