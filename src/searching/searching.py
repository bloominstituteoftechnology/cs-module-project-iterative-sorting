def linear_search(arr, target):
    # for each element in the given arr, check if the i element equals the given target.
    # if the target is in the ith element than return which element that target is at
    # in the array. If the target is not found in the array then return -1.
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # compare the target to the midpoint value of an array.
    # if it is equal to the target then return that array. 
    # if it is less than the target then we need to make the midpoint the new low
    # end for searching. If it is greater than the target than we need to make the midpoint
    # the new high end for searching. Once we have the new low or high point we will 
    # looping back over the new arrays until we find the target. 
    # if the target isnt in the array then return -1. 

    low = 0
    high = len(arr) -1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1  # not found
