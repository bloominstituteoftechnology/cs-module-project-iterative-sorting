#prefix sum array saves times in calculations of an array

A = [6,3,-2,4,-1,0, -5]
def calculate(A, K):
    for i in range(1,len(A)):
        if i != 0:
            A[i] = A[i] + A[i-1]
    print(A)
    # calculate range 0 - 6
    return A[K]

print(calculate(A, 4))



A = [6,3,-2,4,-1,0, -5]
def calculate1(A, K, J):
    for i in range(1,len(A)):
        if i != 0:
            A[i] = A[i] + A[i-1]
    print(A)
    A
    return A[J] - A[K - 1]
 
    
#calculate range [2,6]
print(calculate1(A, 2, 6))