# A non-empty array A consisting of N integers is given.

# The leader of this array is the value that occurs in more than half of the elements of A.

# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:

# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

# For example, given:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

def equi(A):
    if len(A) == 2 and A[0] == A[1]:
        return 1
    if len(A) == 2 and A[0] != A[1]:
        return 0
    original = [e for e in A]
    #find leader
    A.sort()
    denom = A[len(A)//2]
    leader_list = []
    for i in range(len(A)):
        if original[i] == denom:
            leader_list.append(i)
    
    if len(leader_list) < len(A) / 2:
        print('55')
        return 0
    
    pointer = 0
    counter = 0
    while pointer <= len(original) - 1:
        left = []
        right = []
        for i in range(len(original)):
            if i <= pointer:
                left.append(original[i])
            else:
                right.append(original[i])
        print('L',left, 'R', right)
        print(left.count(denom), (len(left) / 2), right.count(denom), (len(right) / 2))
        if left.count(denom) > (len(left) / 2) and right.count(denom) > (len(right) / 2):
            counter += 1
            print('counter', counter)
        pointer += 1
    return counter

    
  
    



A = [4,3,4,4,4,2]
print(equi(A))