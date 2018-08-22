num = int(input("Enter the number of Fibonacci series to generate: "))

def fib(n):
    t1 = 0
    t2 = 1
    fibSeries = []
    for i in range(0, n):
        fibSeries.append(t1)
        nextterm = t1 + t2
        t1 = t2
        t2 = nextterm
    return fibSeries

print(fib(num))