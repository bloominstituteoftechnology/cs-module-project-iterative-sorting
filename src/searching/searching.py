def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    mid = 0
    right = len(arr) - 1
  
    while left <= right: 
        # set mid to sum of h & l with floor division
        mid = (right + left) // 2
        # check if target is at mid 
        if arr[mid] < target: 
            left = mid + 1
        # if target is greater, ignore left half 
        elif arr[mid] > target: 
            right = mid - 1
        # if target is smaller, ignore right half 
        else: 
            return mid 

    return -1  # not found
