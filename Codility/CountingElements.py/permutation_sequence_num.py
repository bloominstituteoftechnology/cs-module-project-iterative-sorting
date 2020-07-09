# A non-empty array A consisting of N integers is given.

# A permutation is a sequence containing each element from 1 to N once, and only once.

# For example, array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.

# The goal is to check whether array A is a permutation.

# Write a function:

# def solution(A)

# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.

# Given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

def permutation(A):
    maxValue = max(A)
    if len(A) != maxValue:
        return 0

    arr = [0 for _ in range(maxValue + 1)]

    for x in A:
        arr[x] += 1
    arr = arr[1:]
    # can only have each value once
    if sum(arr) == maxValue and 0 not in arr:
        return 1
    else:
        return 0

A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8] 
print(permutation(A))