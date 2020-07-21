def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
        print(max_slice)
    return max_slice

A = [5,-7,3,2,5,9]
print(golden_max_slice(A))

# A non-empty array A consisting of N integers is given.

# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

# For example, array A such that:

#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# contains the following example double slices:

# double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
# double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
# double slice (3, 4, 5), sum is 0.
# The goal is to find the maximal sum of any double slice.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

# For example, given:

#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# the function should return 17, because no double slice of array A has a sum of greater than 17.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−10,000..10,000].
#https://www.martinkysel.com/codility-maxdoubleslicesum-solution/
def double_slice(A):
    #slice forward
    # forward = []
    # mValue = 0
    # for i in range(1, len(A)-1):
    #     mValue = max(mValue+A[i], A[i])
    #     forward.append(mValue) 
    # print(forward)

    # backward = []
    # mValueB = 0
    # for i in range(len(A)-2, 0, -1):
    #     mValueB = max(mValueB+A[i], A[i])
    #     backward.append(mValueB) 
    # print(backward)


    forward = [0 for _ in range(len(A))]
    backward = [0 for _ in range(len(A))]
    for i in range(1, len(A)):
        forward[i] = max(0,forward[i-1]+ A[i])
        
    print(forward)

    # backward = []
    # mValueB = 0
    # for i in range(len(A)-2, 0, -1):
    #     mValueB = max(mValueB+A[i], A[i])
    #     backward.append(mValueB) 
    # print(backward)
        
        
     

A = [3, 2, 6, -1, 4, 5, -1, 2]
#print(double_slice(A))