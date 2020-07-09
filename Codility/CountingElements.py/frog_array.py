# A small frog wants to get to the other side of a river. The frog is initially located on one bank
#  of the river (position 0) and wants to get to the opposite bank (position X+1).
#  Leaves fall from a tree onto the surface of the river.

# You are given an array A consisting of N integers representing the falling leaves. 
# A[K] represents the position where one leaf falls at time K, measured in seconds.

# The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

# For example, you are given integer X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

# Write a function:

# def solution(X, A)

# that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

# If the frog is never able to jump to the other side of the river, the function should return −1.

# For example, given X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# the function should return 6, as explained above.

# Write an efficient algorithm for the following assumptions:

# N and X are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..X].

def frog_jump(X, A):

    #given value, need to find index
    # #if can't jump return -1
    # jump = -1
    # #
    # required_positions = [0 for _ in range(0, X+1)]
    # print(required_positions)
   
    # for i in range(0, len(A)):
        
    #     #putting all previous positions in array
    #     if A[i] <= X and required_positions[A[i]] == 0:      
    #         required_positions[A[i]] += 1 
    #         print(required_positions)
    #         if sum(required_positions) == X:
    #             jump = i
    #             return jump  
    # return jump
        









#63%
 #if can't jump return -1
    jump = -1
    #length of zeros = required positions
    required_positions = [x for x in range(1, X + 1)]

   
    for i in range(0, len(A)):
        print(required_positions)
        #putting all previous positions in array
        if A[i] in required_positions:
            required_positions.remove(A[i]) 
            if len(required_positions) == 0:
                #looks for second array is cleared
                jump = i
                return jump  
    return jump

A = [1,3,5,2,3,5,4]
#print(frog_jump(5,A))


def frog2(X,A):
    # set counter 
    position = set()
    #enumerate gives a built in counter
    for i,j in enumerate(A):
        position.add(j)
        print(position)
        if len(position) == X:
            return i
    return -1

print(frog2(5,A))
