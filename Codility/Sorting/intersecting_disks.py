# We draw N discs on a plane. The discs are numbered from 0 to N − 1. 
# An array A of N non-negative integers, specifying the radiuses of the discs, 
# is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th 
# and K-th discs have at least one common point (assuming that the discs contain 
# their borders).

# The figure below shows discs drawn for N = 6 and A as follows:

#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0


# There are eleven (unordered) pairs of discs that intersect, namely:

# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:

# def solution(A)

# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Given array A shown above, the function should return 11, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].
#https://rafal.io/posts/codility-intersecting-discs.html
#https://codesays.com/2014/solution-to-beta2010-number-of-disc-intersections-by-codility/
def disks(A):
    count = 0
    #compare to other disks
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] + A[j]) >= (j - i):
                # print('(A[i] + A[j])', (A[i] + A[j]))
                # print('(j - i)', (j - i))
                count += 1
                # print(count)
    return count




A = [1,5,2,1,4,0]
#print(disks(A))

def disks2(A):
    low_range = []
    #start of disks
    for i in range(len(A)):
        low_range.append(i - A[i])
    print('low_range',low_range)

    start = [0 for _ in range(max(low_range) + 1)]
    for i in range(len(low_range)):
        
        if low_range[i] <= 0:
            start[0] += 1
        else:
            start[low_range[i]] += 1
    #print(start)
    count = 0
    for i in range(len(A)):
        if (i - A[i]) < 0:
            s = 0
        else:
            s = (i - A[i])
        print(sum(start[s: (i+A[i])+1]) - 1)
        count += (sum(start[s: (i+A[i])+1]) - 1)
    return count
    # if i in range(len(low_range)):
    #     if low_range[i] < 0:

    # print('low_range', low_range)
    # print(low_range[1: 2])

A = [1,5,2,1,4,0]
print(disks2(A))
# def disks1(A):
#     count = 0
#     low_range = []
#     high_range = []

#     for i in range(len(A)):
#         low_range.append(i - A[i])
#     for i in range(len(A)):
#         high_range.append(i + A[i])
    
#     low_range.sort()
#     print(low_range)
#     high_range.sort()
#     print(high_range)

#     open = []
#     for x in low_range:
#         if x > min(high_range):
#             for j in high_range:
#                 if high_range[j] < x:
#                     high_range.remove(high_range[j])
#         open.append(x)
#         count += len(A) - 1
#     #compare to other disks
    # for i in range(len(A)):
    #     for j in range(i+1, len(A)):
    #         if (A[i] + A[j]) >= (j - i):
    #             # print('(A[i] + A[j])', (A[i] + A[j]))
    #             # print('(j - i)', (j - i))
    #             count += 1
    #             # print(count)
    # return count




A = [1,5,2,1,4,0]
#print(disks1(A))


