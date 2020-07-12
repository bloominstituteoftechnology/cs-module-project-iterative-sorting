# The Fibonacci sequence is defined using the following recursive formula:

#     F(0) = 0
#     F(1) = 1
#     F(M) = F(M - 1) + F(M - 2) if M >= 2
# A small frog wants to get to the other side of a river. The frog is initially located 
# at one bank 
# of the river (position −1) and wants to get to the other bank (position N).
#  The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. 
# Luckily, there are many leaves on the river, and the frog can jump between the leaves,
#  but only in the direction of the bank at position N.

# The leaves on the river are represented in an array A consisting of N integers.
#  Consecutive elements of array A represent consecutive positions from 0 to N − 1 
# on the river. 
# Array A contains only 0s and/or 1s:

# 0 represents a position without a leaf;
# 1 represents a position containing a leaf.
# The goal is to count the minimum number of jumps in which the frog can get to 
# the other side of the river (from position −1 to position N).
#  The frog can jump between positions −1 and N (the banks of the river) and every
#  position containing a leaf.

# For example, consider array A such that:

#     A[0] = 0
#     A[1] = 0
#     A[2] = 0
#     A[3] = 1
#     A[4] = 1
#     A[5] = 0
#     A[6] = 1
#     A[7] = 0
#     A[8] = 0
#     A[9] = 0
#     A[10] = 0
# The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

# Write a function:

# class Solution { public int solution(int[] A); }

# that, given an array A consisting of N integers, returns the minimum number of 
# jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

# For example, given:

#     A[0] = 0
#     A[1] = 0
#     A[2] = 0
#     A[3] = 1
#     A[4] = 1
#     A[5] = 0
#     A[6] = 1
#     A[7] = 0
#     A[8] = 0
#     A[9] = 0
#     A[10] = 0
# the function should return 3, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.


def frog_fib(A):
    #N in len of array
    # move from -1 to N
    # what is the max frog can jump?
   N = len(A)
   print(N)

    #find fib numbers
   fib = [0] * (N )
  
    
   fib[1] = 1
   limit = 0
  
   for i in range(2, N):
      fib[i] = fib[i - 1] + fib[i - 2]
   fib
   print(fib)
   if N in fib:
      return 1

   options = []
   for i in range(len(A)):
      if A[i] ==1:
         options.append(i+1)
   print(options)
   crossed = False
   jumps = 0
   distance = N
   while crossed == False and distance <= 0:
      for o in options:
         if options[o] in fib:
            jumps += 1
            distance -= options[o]
            options = [x - options[o] for x in options]
         if distance >= 0:
            crossed == True
   return jumps
   # newFib = []
   
   # #look for full jump then go backwards
   # jumpsTable = [0 for _ in range(N + 1)]
   # if N in fib:
   #    return 1
   
   # above = False
   # lowest = N
   # for x in fib:
   #    all = x
   #    count = 1
   #    while above == False:
   #       print('all', all, 'count', count)
   #       for j in fib:
   #          if all + j >= N:
   #             count += 1
   #             above = True
   #             print(above)
   #             break
   #          else:
   #             count += 1
   #             all = all + j
   #    if count < lowest:
   #       lowest = count
   # return lowest
     
   
   

    #fib jump lengths
  
   #  if n <= 1:
   #     return n
   #  else:
   #     return(recur_fibo(n-1) + recur_fibo(n-2))

   #  nterms = 10

   #  # check if the number of terms is valid
   #  if nterms <= 0:
   #  print("Plese enter a positive integer")
   #  else:
   #  print("Fibonacci sequence:")
   #  for i in range(nterms):
   #     print(recur_fibo(i))




A = [0,0,0,1,1,0,1,0,0,0,0]
print(frog_fib(A))