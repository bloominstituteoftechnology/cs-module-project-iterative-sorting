# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer 
# (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# negative

def missing_num(A):
    maxValue = max(A)
    array = [0 for _ in range(maxValue + 1)]
    #incase last is missing
    missing = len(A) + 1

    if maxValue < 1:
        missing = 1
        return 1

    for x in A:
        if x > 0:
            array[x] += 1
    for i in range(1, len(array)):
        if array[i] == 0:
            missing = i
            return missing
    return missing



A = [4, 5, 6, 2]
print(missing_num(A))
