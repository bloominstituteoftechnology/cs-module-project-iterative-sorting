# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

def divis2(A, B, K):
    # B/K all dividors 
    #disregard A/k results, to floor
    diff = B/K - A//K
    #if divides evenly, do not disregard final value of A/K
    if A%K == 0:
        diff += 1
        
    return int(diff)
    
print(divis2(11, 14, 2))



def divis(A, B, K):
    count = 0
    for x in range(A, B+1):
        print(x)
        if x%K==0:
            count += 1
    return count



#print(divis(6, 11, 2))
import math

#find the first number that is divisable by K
#then calculate how many remaining numbers will be divisable by k,
#  and add that sum to the first one
def divis1(A, B, K): 
    count = 0
    first = 0
    if A%K == 0:
        first = A
    else:
        first = A + A%K
    print('first', first)
    diff = B - first
    print(diff)
    #count = math.floor(diff/K + 1)
    count = (diff//K) + 1

    

    return count

print(divis1(5, 11, 2))


