# Two positive integers N and M are given. Integer N represents the number
#  of chocolates arranged in a circle, numbered from 0 to N − 1.

# You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

# You begin with eating chocolate number 0. Then you omit the next M − 1 
# chocolates or wrappers on the circle, and eat the following one.

# More precisely, if you ate chocolate number X, then you will next eat
#  the chocolate with number (X + M) modulo N (remainder of division).

# You stop eating when you encounter an empty wrapper.

# For example, given integers N = 10 and M = 4. You will eat the following
#  chocolates: 0, 4, 8, 2, 6.

# The goal is to count the number of chocolates that you will eat,
#  following the above rules.

# Write a function:

# def solution(N, M)

# that, given two positive integers N and M, returns the number of chocolates
#  that you will eat.

# For example, given integers N = 10 and M = 4. the function should return 5,
#  as explained above.

# Write an efficient algorithm for the following assumptions:

# N and M are integers within the range [1..1,000,000,000].

def chocolate(N ,M):
    if N == 1:
        return 1
    nums = [0 for _ in range(N)]
   
    nums[0] = 1
    #nums[M] = 1
    count = 1
    position = M%N
    # print(nums)
    current = nums[position]
    #print('position',M%N, 'current',  current)
    while current == 0 and count <= N:
        count += 1
        nums[position] = 1
        position = (position + M)%N
        current = nums[position]
        print(nums)

        
    return count

N = 2
M = 1
print(chocolate(N, M))