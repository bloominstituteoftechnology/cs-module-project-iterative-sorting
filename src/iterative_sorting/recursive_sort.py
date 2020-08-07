

def countdown(n):
    # base case note - basecase is not always first
    if n == 0: #basecase 
        return
    print(n)
    countdown(n-1)
    countdown(n-1)

countdown(3)

# Fibonacci sequence 
# fib(n) = fib(n-1) + fib(n-2)
# 1,1,2,3,5,8,13...
# base case 
    # if n == 0 return 0
    # if n == 1 return 1
# resursion step
    # return fib(n-1) + fib(n-2)

def fib(n):
    # basecase
    if n == 0:
        return 0
    if n == 1:
        return 1
    n_minus_1 = fib(n-1)
    n_minus_2 = fib(n-2)
    print(n_minus_1 + n_minus_2)
    return n_minus_1 + n_minus_2

fib(2)

