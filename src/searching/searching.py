def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    n = len(arr)
    low = 0
    high = n-1
    while low <= high:
        middle = (low + high)//2
        if target < arr[middle]:
            high = middle-1 # eliminate RHS
        elif target > arr[middle]:
            low = middle+1 # eliminate LHS
        else:
            return middle        
    return -1  # not found
