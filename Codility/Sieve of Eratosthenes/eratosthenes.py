#The Sieve of Eratosthenes is a very simple and popular technique for finding all the prime
#numbers in the range from 2 to a given number n
def sieve(n):
    sieve = [True for _ in range(n+1)]
    #0 and 1 not considered prime
    sieve[0] = sieve[1] = False
    # start at 2
    i = 2
    while(i * i <= n):
        print('i',i)
        if (sieve[i]):
            k = i * i
            while k <= n:
                print('k', k)
                sieve[k] = False
                k += i
        i += 1
    return sieve



n = 20
print(sieve(n))

#Factorization
#find smallest prime factorials 
def arrayF(n):
    F = [0] * (n+1)
    i = 2
    while (i*i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i
                k += i
        i += 1
    print(F)

n = 20
print(arrayF(n))

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x /= F[x]
    primeFactors += x
    return primeFactors