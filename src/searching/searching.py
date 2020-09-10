def linear_search(arr, target):
    # Your code here
    iteration = -1
    for i in arr:
        iteration += 1
        if i == target:
            return iteration
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1
    middle = 0
    while low <= high:
        middle = (low + high) // 2
        if target < arr[middle]:
            high = middle - 1  # Remove right
        elif target > arr[middle]:
            low = middle + 1  # Remove left
        else:
            return middle
    return -1  # not found