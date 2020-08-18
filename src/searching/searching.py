def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    # Not found
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high + low) // 2        
        if arr[middle] > target:
            high = middle - 1
        elif arr[middle] < target:
            low = middle + 1
        else:
            return middle
            
    return -1  # not found
