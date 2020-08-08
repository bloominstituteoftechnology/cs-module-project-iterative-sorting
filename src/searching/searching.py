def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            # found
            return i
    # not found
    return -1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    first = 0
    last = len(arr) - 1

    while first <= last:

        middle = (first + last) // 2

        if arr[middle] == target:
            # return index of target not the value
            return middle
        else:
            if target < arr[middle]:
                # if target is less than the value of the mid element, make the element before the middle the last element to search through
                last = middle - 1
            else:
                # if the target is greater than the middle element, make one after the middle element the starting point for the next search
                first = middle + 1
    # Same as returning false
    return -1

import random
import time
# 100,000 --> 50,000 Log(100,000)
# linear search
# keywords: unsorted and random
"""
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
"""

# binary search
# keywords: sorted, ordered
"""
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
"""
