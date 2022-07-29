# An array A consisting of N different integers is given.
#  The array contains integers in the range [1..(N + 1)],
#  which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

def missing_integer(A):
    
    
    #Edge case if empty array 
    if len(A)  == 0:
        missing_integer = 1
        return missing_integer
        
    
    if len(A) > 0:
        #if single and not 1
        if len(A) == 1 and A[0] != 1:
            missing_integer = 1
            return missing_integer

        #Edge if array of 1 value
        if len(A) == 1:
            missing_integer = A[0] + 1
            return missing_integer
    
        
        maxValue = max(A)
        #Edge, missing last item
        # set missing_inter to last item, can be overwritten below
        missing_integer = maxValue + 1

        #range of zeros from 0 to maxValue
        values = [0 for _ in range(maxValue + 1)]
   
    
        for x in A:
            values[x] += 1
        
        # start at 1, not zero per instructions
        #Edge if 1 is missing, return 1
        
    

        for i in range(1, len(values)):
            if values[i] == 0:
                missing_integer = i
        
    return missing_integer
A = []
print(missing_integer(A))