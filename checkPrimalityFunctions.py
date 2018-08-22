num = int(input("Enter a number: "))

def isPrime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False

if(isPrime(num)):
    print("Prime")
else:
    print("Not Prime")