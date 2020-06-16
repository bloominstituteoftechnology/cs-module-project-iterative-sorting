def linear_search(arr, target):
    for i in range(len(arr)): # loop over every element, one by one
        if arr[i] == target: # if the element is equal to the target
            return i # then return the element
    return -1 # not found (target was not in the array)

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0 # declare a starting point
    high = len(arr)-1 # declare an ending point
    mid = 0 # declare a mid point for now
    while high >= low: # loop
        mid = (high + low) // 2 # find the mid point
        if arr[mid] > target: # if the mid point is greater than the target
            high = mid - 1 # ignore one side of the array
        elif arr[mid] < target: # if the mid point is less than the target
            low = mid + 1 # ignore one side of the array
        else: # if the mid point is the target
            return mid # return the mid point
    return -1 # not found (target was not in the array)