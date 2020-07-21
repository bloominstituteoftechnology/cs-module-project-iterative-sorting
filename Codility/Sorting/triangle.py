# An array A consisting of N integers is given. A triplet (P, Q, R)
#  is triangular if 0 ≤ P < Q < R < N and:

# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# For example, consider array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# Triplet (0, 2, 4) is triangular.

# Write a function:

# class Solution { public int solution(int[] A); }

# that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

# For example, given array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# the function should return 1, as explained above. Given array A such that:

#   A[0] = 10    A[1] = 50    A[2] = 5
#   A[3] = 1
# the function should return 0.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

def triangle(A):
    #values closest together are more likely to make a triangle
    print(A)
    #put in order
    A.sort()
    print(A)
    good = 0
    pointer = 0
    while pointer <= len(A) - 3:
        if A[pointer] + A[pointer + 1] > A[pointer + 2] and A[pointer + 1] + A[pointer + 2] > A[pointer] and A[pointer + 2] + A[pointer] > A[pointer + 1]:
            good += 1
        pointer += 1
    if good > 0:
        return 1
    else:
        return 0

A = [5, 3, 3]
print(triangle(A))