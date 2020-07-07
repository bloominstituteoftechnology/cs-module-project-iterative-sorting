# A non-empty Aay A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

# For example, array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:

# (0, 1, 2), product is −3 * 1 * 2 = −6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.

# Write a function:

# def solution(A)

# that, given a non-empty array A, returns the value of the maximal product of any triplet.

# For example, given array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

def max_product(A):
    if len(A) < 4:
        max_array = A[0] * A[1] * A[2]
        return max_array
     
    normal = A
    normal.sort()
    print(normal)

    
    top2_b1 = 0
    top2_b2 = 0
    bottom2_top1 = 0
    
    if len(A) > 3:
        #put in a list
        top_bottom4 = [A[0], A[1], A[2],A[-3],  A[-2], A[-1]]
        
        bottom3 = top_bottom4[0] * top_bottom4[1] * top_bottom4[2]

        top3 = top_bottom4[-1] * top_bottom4[-2] * top_bottom4[-3]
        print('top3', top3, 'bottom3', bottom3)
        
        
        bottom2_top1 = top_bottom4[0] * top_bottom4[1] * top_bottom4[-1]
          
          
   
    max_array = [bottom3, top3, bottom2_top1]
    
    maxValue = max(max_array)
    return maxValue
    


A =  [4, 5, 1, 0]

print(max_product(A))



