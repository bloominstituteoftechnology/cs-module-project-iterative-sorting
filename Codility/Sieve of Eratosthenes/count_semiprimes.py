# A prime is a positive integer X that has exactly two distinct divisors: 1 and X. 
# The first few prime integers are 2, 3, 5, 7, 11 and 13.

# A semiprime is a natural number that is the product of two 
# (not necessarily distinct) prime numbers. The first few semiprimes 
# are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# You are given two non-empty arrays P and Q, each consisting of M integers. 
# These arrays represent queries about the number of semiprimes within specified ranges.

# Query K requires you to find the number of semiprimes within the range
#  (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

# For example, consider an integer N = 26 and arrays P, Q such that:

#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20
# The number of semiprimes within each of these ranges is as follows:

# (1, 26) is 10,
# (4, 10) is 4,
# (16, 20) is 0.
# Write a function:

# def solution(N, P, Q)

# that, given an integer N and two non-empty arrays P and Q consisting of M integers,
#  returns an array consisting of M elements specifying the consecutive 
# answers to all the queries.

# For example, given an integer N = 26 and arrays P, Q such that:

#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20
# the function should return the values [10, 4, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..50,000];
# M is an integer within the range [1..30,000];
# each element of arrays P, Q is an integer within the range [1..N];
# P[i] ≤ Q[i].

def solution(N, P, Q):
    #find primes with range
    if N == 0 or N == 1:
        all_zeros = [0 for _ in range(len(P))]
        return all_zeros
    maxvalue = max(P+Q)
    sieve = [True for _ in range(maxvalue+1)]
    sieve[0] = sieve[1] = False
    i = 2
    while(i*i <= maxvalue):
        if (sieve[i]):
            k = i * i
            while k <= maxvalue:
                sieve[k] = False
                k += i
        i += 1
    primes = []
    for i in range(len(sieve)):
        if sieve[i] == True:
            primes.append(i)
    
    #make arrays half of N
    primes_half = []
    for x in primes:
        if x <= N/2:
            primes_half.append(x)
    #print(primes_half)
    semi = []
    for x in primes_half:
        for j in primes_half:
            if x * j <= maxvalue:
                semi.append(x*j)
    
    semi_set = list(set(semi))
    print('semi',semi_set)
    #print(semi_set)
    isPrime = [0 for _ in range(max(semi_set)+1)]
    for x in semi_set:
        isPrime[x] = 1
    #print(isPrime)
    results = []
    for i in range(len(P)):
        results.append(sum(isPrime[P[i]:Q[i]+1]))
    return results






N = 26
P = [1,4,16]
Q = [26,10,20]
print(solution(N, P, Q))


def solution1(N, P, Q):
    #find primes with range
    if N == 0 or N == 1:
        all_zeros = [0 for _ in range(len(P))]
        return all_zeros
    maxvalue = max(P+Q)
    sieve = [True for _ in range(maxvalue+1)]
    sieve[0] = sieve[1] = False
    i = 2
    while(i*i <= maxvalue):
        if (sieve[i]):
            k = i * i
            while k <= maxvalue:
                sieve[k] = False
                k += i
        i += 1
    primes = []
    semi = []
    for i in range(len(sieve)):
        if sieve[i] == True and i <= N/2:
            primes.append(i)
            for x in primes: 
                if x * i <= maxvalue:
                    semi.append(x * i)
     
    
    semi_set = list(set(semi))
    #print(semi_set)
    isPrime = [0 for _ in range(max(semi_set)+1)]
    for x in semi_set:
        isPrime[x] = 1
    #print(isPrime)
    results = []
    for i in range(len(P)):
        results.append(sum(isPrime[P[i]:Q[i]+1]))
    return results






N = 26
P = [1,4,16]
Q = [26,10,20]
print(solution1(N, P, Q))

