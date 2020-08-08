def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found

import random
import time
# 100,000 --> 50,000 Log(100,000)
# linear search
# keywords: unsorted and random

my_range = 100
my_size = 10

my_random = random.sample(range(my_range), my_size)
print(my_random)

searching_for = 3

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
        return False

print(linear_search(my_random, searching_for))

# binary search
# keywords: sorted, ordered

def find_value_binary(arr, value):
    first = 0
    last = len(arr)-1

    found = False

    while first <= last and not found:
        middle = (first + last) // 2

        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found
print(find_value_binary(my_random, searching_for))

