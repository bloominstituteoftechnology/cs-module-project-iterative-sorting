def linear_search(arr, target):
    for i in range(len(arr)): 
  
        if arr[i] == target: 
            return i 

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == target:
            return midpoint
        elif target < midpoint_value:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return -1  # not found
