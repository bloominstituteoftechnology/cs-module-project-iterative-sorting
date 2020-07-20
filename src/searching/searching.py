def linear_search(arr, target):
    for element in range (0, len(arr)):
        if arr[element] == target:
            return element
    
    return -1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low+high)//2
        if target < arr[middle]:
            high = middle - 1 # eliminate RHS
        elif target > arr[middle]:
            low = middle + 1 #eliminate LHS
        else:
            return middle
    
    return -1

