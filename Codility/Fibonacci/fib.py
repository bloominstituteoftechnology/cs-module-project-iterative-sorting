def fibonacci(n):
    #print(n)
    if (n <= 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))

def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        print(fib)
    return fib[n]
print(fibonacciDynamic(20))