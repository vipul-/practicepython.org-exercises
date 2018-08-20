word = input("Enter a word to check for palindrome: ")

reverse = word[::-1]

if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")