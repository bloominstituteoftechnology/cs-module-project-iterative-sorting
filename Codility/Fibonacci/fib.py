#Fibonacci - add last two numbers together

def fibonacci(n):
    #print(n)
    if (n <= 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))

def fibonacciDynamic(n):
    #make a list of zeros, 
    fib = [0] * (n + 1)
    
    fib[1] = 1
    print(fib)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
       # print(fib)
    return fib[n]
print(fibonacciDynamic(20))

#recursion
def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)
print(fib_rec(20))