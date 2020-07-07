# You are given N counters, initially set to 0, and you have two possible operations on them:

# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given. This array represents consecutive operations:

# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:

#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.

# Write a function:

# def solution(N, A)

# that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

# Result array should be returned as an array of integers.

# For example, given:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.

# Write an efficient algorithm for the following assumptions:

# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].

def counter(N, A):
    counter = [0 for _ in range(N)]
    pointer = 0
    while pointer < len(A):
        if A[pointer] <= N:
            counter[A[pointer] - 1] += 1
            print(counter)
            pointer += 1
        elif A[pointer] > N:
            maxValue = max(counter)
            counter = [maxValue for _ in range(N)]
            print(counter)
            pointer += 1
    return counter





A = [3,4,4,6,1,4,4]
#print(counter(5, A))

#66%
# for x in A:
#         if x <= N:
#             counter[x - 1] += 1
#             print(counter)
#         elif x > N:
#             maxValue = max(counter)
#             counter = [maxValue for _ in range(N)]
#             print(counter)
#     return counter


def solution(N, A):
    counter = [0 for _ in range(N)]    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > counter[command-1]:
                # lazy write
                counter[command-1] = max_counter
            counter[command-1] += 1
            
            if current_max < counter[command-1]:
                current_max = counter[command-1]
            print('counter',counter)
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
            print(max_counter)
    for index in range(0,N):
        if counter[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            counter[index] = max_counter
    return counter
A = [3,4,4,6,1,4,4]
print('solution', counter(5, A))