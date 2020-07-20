# You are given integers K, M and a non-empty array A consisting of N integers. 
# Every element of the array is not greater than M.

# You should divide this array into K blocks of consecutive elements. 
# The size of the block is any integer between 0 and N.
#  Every element of the array should belong to some block.

# The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. 
# The sum of empty block equals 0.

# The large sum is the maximal sum of any block.

# For example, you are given integers K = 3, M = 5 and array A such that:

#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# The array can be divided, for example, into the following blocks:

# [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
# [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
# [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
# [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
# The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

# Write a function:

# class Solution { public int solution(int K, int M, int[] A); }

# that, given integers K, M and a non-empty array A consisting of N integers, 
# returns the minimal large sum.

# For example, given K = 3, M = 5 and array A such that:

#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# the function should return 6, as explained above.

# Write an efficient algorithm for the following assumptions:

# N and K are integers within the range [1..100,000];
# M is an integer within the range [0..10,000];
# each element of array A is an integer within the range [0..M].
def solution(K, M, A):
    if K == 1:
        return sum(A)
    if len(A) == 2 and K >= 2:
        return max(A)
    if len(A) == K:
        return max(A)
    if K >= len(A):
        return max(A)
    sortArr = sorted(A)
    if sortArr[-1] >= sum(sortArr[:-1]):
        return sortArr[-1]
    if K > 2 and sortArr[-1] + sortArr[0] >= sum(sortArr[1:-1]):
        return sortArr[-1] + sortArr[0]
    print(sortArr)
    p1 = 0
   # p2 = len(A)-1
    arrays = []
    #print(arrays)
    high = [sortArr[-1]]
    mid = [sortArr[-2], sortArr[0]]
    lower = sortArr[:-1]
    while sum(high) < sum(lower) and sum(mid) < sum(high):
        ##print(sortArr[p1], sortArr[p2])
        print(sortArr[p1])
        high.append(sortArr[p1])
        mid.append(sortArr[p1 + 1])
        print(mid)
        lower.remove(sortArr[p1])
        p1 += 1
        # arrays.append(sortArr[p2])
        # arrays.append(sortArr[p1])
        
    #     #print(arrays)
    #     p1 += 1
    #     p2 -= 1
    # print(arrays)
    # dividor = len(A)//K 
    # return sum(arrays[0:dividor])
    if sum(mid) > sum(high):
        return sum(mid)
    else:
        return sum(high)
        


K = 3
M = 6
A = [5, 2, 3, 4, 6]
print(solution(K, M, A))



25%
def solution(K, M, A):
    # write your code in Python 3.6
    if K == 1:
        return sum(A)
    if len(A) == 2 and K >= 2:
        return max(A)
    if len(A) == K:
        return max(A)
    if K >= len(A):
        return max(A)
    sortArr = sorted(A)
    if sortArr[-1] >= sum(sortArr[:-1]):
        return sortArr[-1]
    if K > 2 and sortArr[-1] + sortArr[0] >= sum(sortArr[1:-1]):
        return sortArr[-1] + sortArr[0]
    print(sortArr)
    p1 = 0
   # p2 = len(A)-1
    arrays = []
    #print(arrays)
    high = [sortArr[-1]]
    mid = [sortArr[-2], sortArr[0]]
    lower = sortArr[:-1]
    while sum(high) < sum(lower) and sum(mid) < sum(high):
        ##print(sortArr[p1], sortArr[p2])
        print(sortArr[p1])
        high.append(sortArr[p1])
        mid.append(sortArr[p1 + 1])
        print(mid)
        lower.remove(sortArr[p1])
        p1 += 1
        # arrays.append(sortArr[p2])
        # arrays.append(sortArr[p1])
        
    #     #print(arrays)
    #     p1 += 1
    #     p2 -= 1
    # print(arrays)
    # dividor = len(A)//K 
    # return sum(arrays[0:dividor])
    if sum(mid) > sum(high):
        return sum(mid)
    else:
        return sum(high)