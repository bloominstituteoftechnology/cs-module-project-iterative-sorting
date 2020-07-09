# A positive integer D is a factor of a positive integer N 
# if there exists an integer M such that N = D * M.

# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the number of its factors.

# For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].

def factors(N):
    i = 1
    count = 0
    # do not need to get factors past the square root.  
    #because factors lower than square root will have one match greater than square root
    # ex.  for 16.  1,16  2,8, 4
    while (i * i <= N):
        print('i', i)
        if (i * i == N):
            count += 1
        #example i = 1 -> count += 2 for 1 and 16
        elif (N % i == 0):
            count += 2   
        i += 1
        
    return count


N = 16
print(factors(N))


#  count = 0
#     for i in range(1,N+1):
#         print(i)
#         if N%i == 0:
#             count += 1
#     return count