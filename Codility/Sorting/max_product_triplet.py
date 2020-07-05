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
    top_three = normal[-3:]
    prod_top = 1
    for x in top_three:
        prod_top *= x
    print('top ',prod_top)

    bottom3 = normal[:3]
    prod_bottom = 1
    for x in bottom3:
        prod_bottom *= x
    print('bottom',prod_bottom)

    
    top2_b1 = 0
    top2_b2 = 0
    bottom2_top1 = 0
    # top_bottom4
    if len(A) > 3:
        #put in a list
        top_bottom4 = [A[0], A[1], A[-1], A[-2]]
        #if last two are negatives, prod will make positive
        if top_bottom4[0] * top_bottom4[1] > 0:
            bottom2_top1 = top_bottom4[0] * top_bottom4[1] * top_bottom4[-1]
            
            top2_b1 = top_bottom4[-1] * top_bottom4[-2] * top_bottom4[0]
            #next two most likely will not be max
            top2_b2 = top_bottom4[-1] * top_bottom4[-2] * top_bottom4[1]

    absolute = [x for x in A]
    for i in range(0, len(A)): 
        while i - 1 >= 0:
            #value of temp 
            #sets temp to previous value
            tempA = absolute[i - 1]
            #sort by absolute value
            if abs(absolute[i]) < abs(tempA):
                #previous = current value
                absolute[i - 1] = absolute[i]
                #make temp current value
                absolute[i] = tempA
                i -= 1
            else:
               
                break
       
    print(absolute)
    #take into account negative numbers
    top_three_abs = absolute[-3:]
    prod_top_abs = 1
    for x in top_three_abs:
        prod_top_abs *= x
    print('top abs',prod_top_abs)

    bottom3_abs = absolute[:3]
    prod_bottom_abs = 1
    for x in bottom3_abs:
        prod_bottom_abs *= x
    print('bottom abs',prod_bottom_abs)
    
  

   
    max_array = [prod_top, prod_bottom, prod_bottom_abs, prod_top_abs, bottom2_top1, top2_b1, top2_b2]
    
    maxValue = max(max_array)
    return maxValue
    


A =  [-10, -2, -4, 9]

print(max_product(A))



#  normal = A
#     normal.sort()
#     top_three = normal[-3:]
#     prod_top = 1
#     for x in top_three:
#         prod_top *= x
#     print('top ',prod_top)

#     bottom3 = normal[:3]
#     prod_bottom = 1
#     for x in bottom3:
#         prod_bottom *= x
#     print('bottom',prod_bottom)

#     absolute = A
#     for i in range(0, len(A)): 
#         while i - 1 >= 0:
#             #value of temp 
#             #sets temp to previous value
#             tempA = absolute[i - 1]
#             #sort by absolute value
#             if abs(absolute[i]) < abs(tempA):
#                 #previous = current value
#                 absolute[i - 1] = absolute[i]
#                 #make temp current value
#                 absolute[i] = tempA
#                 i -= 1
#             else:
               
#                 break
       
#     print(absolute)
#     #take into account negative numbers
#     top_three_abs = absolute[-3:]
#     prod_top_abs = 1
#     for x in top_three_abs:
#         prod_top_abs *= x
#     print('top abs',prod_top_abs)

#     bottom3_abs = absolute[:3]
#     prod_bottom_abs = 1
#     for x in bottom3_abs:
#         prod_bottom_abs *= x
#     print('bottom abs',prod_bottom_abs)

#     max_array = [prod_top, prod_bottom, prod_bottom_abs, prod_top_abs]
#     maxValue = max(max_array)
#     return maxValue