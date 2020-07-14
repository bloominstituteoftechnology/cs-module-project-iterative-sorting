# You are given an array A consisting of N integers.

# For each number A[i] such that 0 ≤ i < N, we want to count the number 
# of elements of the array that are not the divisors of A[i].
#  We say that these elements are non-divisors.

# For example, consider integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# For the following elements:

# A[0] = 3, the non-divisors are: 2, 6,
# A[1] = 1, the non-divisors are: 3, 2, 3, 6,
# A[2] = 2, the non-divisors are: 3, 3, 6,
# A[3] = 3, the non-divisors are: 2, 6,
# A[4] = 6, there aren't any non-divisors.
# Write a function:

# def solution(A)

# that, given an array A consisting of N integers,
#  returns a sequence of integers representing the amount of non-divisors.

# Result array should be returned as an array of integers.

# For example, given:

#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# the function should return [2, 4, 3, 2, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..50,000];
# each element of array A is an integer within the range [1..2 * N].

def total_non(A):
    totals = []
    maxValue = max(A)
    #make cache
    cache = [0 for _ in range(maxValue + 1)]
    for i in range(len(A)):
        count = 0
        #check cache for repeats
        if cache[A[i]] > 0:
            totals.append(cache[A[i]])
        else:
            for j in A:
                if j > A[i]:
                    count += 1
                elif A[i]%j != 0:
                    count += 1
            cache[A[i]] = count
            #print('cache',cache)
            totals.append(count)
            #print('ttals', totals)
    return totals
        


A = [3,1,2,3,6]
print(total_non(A))