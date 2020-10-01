import random

random = random.sample(range(20), 20)
target = 10


def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        mid = (first + last) // 2
        
        if arr[mid] == target:
            return mid
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1 # not found