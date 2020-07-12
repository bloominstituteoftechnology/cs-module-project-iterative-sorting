# You are given two non-empty arrays A and B consisting of N integers.
#  Arrays A and B represent N voracious fish in a river, ordered downstream along the 
# flow of the river.

# The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, 
# then fish P is initially upstream of fish Q. Initially, each fish has a unique position.


# Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish.
#  All its elements are unique. Array B contains the directions of the fish. 
# It contains only 0s and/or 1s, where:

# 0 represents a fish flowing upstream,
# 1 represents a fish flowing downstream.
# If two fish move in opposite directions and there are no other (living) fish between them,
#  they will eventually meet each other. Then only one fish can stay alive − 
# the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet
#  each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them.
#  After they meet:

# If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
# If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
# We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

# For example, consider arrays A and B such that:

#   A[0] = 4    B[0] = 0
#   A[1] = 3    B[1] = 1
#   A[2] = 2    B[2] = 0
#   A[3] = 1    B[3] = 0
#   A[4] = 5    B[4] = 0
# Initially all the fish are alive and all except fish number 1 are moving upstream
# . Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

# Write a function:

# def solution(A, B)

# that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

# For example, given the arrays shown above, the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000];
# each element of array B is an integer that can have one of the following values: 0, 1;
# the elements of A are all distinct.

def solution(A, B):
    stack = []
    oneIndex = []
    if len(B) == 1:
        return 1
    if len(B) == 2 and B[0] == 1 and B[1] == 0:
        return 1
    if len(B) == 2 and B[0] == 0 and B[1] == 1:
        return 2 
    
    for i in range(len(B)):
        #print('i',i)
        if len(stack) == 0 and B[i] == 0:
            stack.append(B[i])
        elif len(stack) == 1 and B[i] == 0:
            stack.append(B[i])
           
        
        #add 1 to stack 
        elif B[i] == 1:
            stack.append(B[i])
            #index used later to compare size
            oneIndex.append(i)
        elif B[i] == 0 and stack[-1] == 0:
            stack.append(B[i])
        #add 0
        ##print('stack -1', stack[-1], A[i] , A[oneIndex[-1]])
        elif B[i] == 0 and stack[-1] == 1 and A[i] > A[oneIndex[-1]]:
            #put 0 on top of stack, then start to compare
            stack.append(B[i])
            #print('stack -2',stack[-2])
            while len(stack) >= 2 and stack[-2] == 1 and stack[-1] == 0:
                if A[i] > A[oneIndex[-1]]:
                    stack.pop(-2)
                    oneIndex.pop()
                else: 
                    #or remove last 0 in stack, because it is less than 1
                    stack.pop(-1)

    #print(stack)
    return len(stack)
          


      
        # elif B[i] == 0 and stack[-1] == 1:
        #     stack.pop()
        #     stack.append(A[i])
        # elif B[i] != B[i-1] and A[i] < A[i-1]:  
        #     while (i-1) >= 0:
        #         if 




A = [3,92,1,5]
B = [0,1]

print(solution(A, B))


# down = 0
#     p1 = 0
#     p2 = len(A)
#     for i in range(len(B)):
#         #find a pair of fish together
#         if B[i] == 1 and B[i + 1] == 0:
#             p1 = i
#             print('p1',p1)
#             p2 = i +1
#             print('p2',p2)
         
#             if A[p1] > A[p2]:
#                 A.remove(A[p2])
#                 print('A',A)
#                 down += 1
#             else:
#                 A.remove(A[p1])
#                 print('A', A)
#                 down += 1
#                 print('down', down)
#                 #look for previous 1
#                 #if previous 1 exists
#                 p2 = p1
#                 print('p2', p2)
#                 p1 = p1 -1
#                 print('p1', p1)
#                     # if 1 in B and p1 != 0:
#                     #     p1 = p1 - 1
#                     #     while p1 >= 0 and B[p1] != 1:
#                     #         p1 = p1 - 1
#                     # else:
#                     #     print('end')
#                     #     break
       
#     alive = len(B) - down          
#     return alive