# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

# For example, consider array A such that:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

# For example, given:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].
def minimal_difference(A):
    # write your code in Python 3.6
    
    minimal_diff = -1
    lowArray = A[0]
    highArray = sum(A) - A[0]
    minimal_diff = abs(lowArray - highArray)
    pointer = 1
    #print('low', lowArray, 'highArray', highArray, minimal_diff)
    while pointer < len(A):
        if len(A) > 2:
            print(lowArray, A[pointer])
            lowArray = lowArray + A[pointer]
            highArray = highArray - A[pointer]
            diff = abs(lowArray - highArray)
            if diff < minimal_diff:
                minimal_diff = diff
            pointer += 1
            print('low', lowArray, 'highArray', highArray, minimal_diff)
        else:
            pointer += 1

    # pointer = 1
    # minimal_diff = -1

    # while pointer < len(A):
    #     lowArray = []
    #     highArray = []
    #     for i in range(0, len(A)):
    #         if i < pointer:
    #             lowArray.append(A[i])
    #             print('Low',lowArray)
    #         else:
    #             highArray.append(A[i])
    #             print('High',highArray)
    #     diff = abs(sum(lowArray) - sum(highArray))
    #     print(diff)
    #     pointer += 1
    #     if minimal_diff < 0 or diff < minimal_diff:
    #         minimal_diff = diff
    return minimal_diff
        
A = [3, 1]
print(minimal_difference(A))