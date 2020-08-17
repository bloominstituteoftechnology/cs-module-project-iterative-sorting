# If we increase input size, how many more steps does the function take?


my_list = [1, 2, 3, 4, 5]

def print_list(arr):
    for thing in arr:
        print(thing)

print_list(my_list) # 5 operations

longer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

print_list(longer_list) # 10 operations
 
 # double input size
 # double the steps
 # this is a one-to-one ratio!
 # linear 
 # O(n)






# Nested loops are quadratic , check it out


def nested_loop(arr):
    for thing in arr:
        for other_thing in arr:
            print(thing, other_thing)


nested_loop(my_list) # takes 25 steps

nested_loop(longer_list) # takes 100 steps

# doubled input size
# quadrupled the number of operations
# quadratic runtime complexity


# count the steps
# calculate Big O


def my_func(arr):
    a = 1 # 1 operation
    b = 2 # 1 operation
    c = a * b # 1 operation

    for x in range(1000): # 1000 elements
        print(x) # 1 operation per element


    for thing in arr: # 5 elements in array
        print(thing) # 1 operation per element

my_func(my_list)

# the above function call has 1008 operations

# 3 + 1000(this is the length of the arr) + 5(this is the length of the arr) = 1008

# O(len(arr))
# O(n)

# Since the loops arent' nested, the n's being counted for big O are at most n*1
# O(n), O(n^2), O(n^3) are much more different than O(n), O(n + 2), O(n + 3)

def two_loops(arr):
    for x in range(10000000000):
        z =  x * x
        print(z)

    for thing in arr:
        print(thing)

    for thing_again in arr:
        print(thing)

# Walking through line by line
## big_num * 2 + len(arr) + len(arr)
## big_num * 2 + (2 * len(arr))
# O(2 * len(arr))
# O(2 * n))
# O(n)




# Challenge
# Classify the run times of each of the following scenarios:
# A. You are searching for a specific name in a phone book (that is sorted alphabetically). B. You meet someone, and they give you their phone number. You realize later that you forgot their name! To match their number with a name, you look through a phone book until you find their phone number.

# Classify the runtimes of each of the following functions:



# A. Problem One
import math

def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)
# 36 ---> 6
# 100 ---> 10
# 10000 ---> 100
# O(log(n))

# example of O(log(n))
def bisect(n): # O(log(n))
    while n > 1 :
        n = n/2

# 100
# 50
# 25
# 12.5
# 6.25
# 3
# 1.5
# 0.75 ~

# A log is finding the number of steps from a number to 1
# logarithmic runtimes are better than linear runtimes because it increases 
# number of operations only by 1 when doubling input



# B. Problem Two 


def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, x):
                for k in range(x, x + 15):
                    sum += 1

# 1463 * (1 + (n * (15 * 1)))
# 1463 * (1 * 15n)
# O(n)
# Disregarding the constants we are left with O(n)

# C. Problem Three



def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print('hi')

# 1 + 1 + n/2 + 1000
# 1002 + n/2
#  O(n/2)
# if n == 2n
# then n/2 == n
# this is NOT log(n)!!!!!!!!!!
# O(log(n)) is the inverse of exponential operations, not multiplication.
# # O(log(n)) is much faster than O(n)
# Logarithmic Runtime Complexity is much faster than Linear Runtime Complexity




# Do both of these functions have the same runtime? (Notice the difference between their inputs)
  
def make_num_pairs(n):
    for num_one in range(n):
        for num_two in range(n):
            print(num_one, num_two)


def make_item_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)


def simple_recurse(n):
    if n <= 1:
        return n
    simple_recurse(n-1)

# o(n) runtime
# this runtime will run as long as the input is large in worst case 
# so Big O notation(worst case notation)
# would be linear or O(n)

# the relation is linear and this is easily discoverable when you check 
# how the output is growing compared to the input


def weird_recurse(n):
    if n <= 1:
        return n
    simple_recurse(n-1) # calling once within itself
    simple_recurse(n-1) # calling once again within itsself

# this is exponential: 2^n
# if there were 3 calls, it would be 3^n











