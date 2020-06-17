def linear_search(arr, target):
    # Your code here
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    min = 0
    max = len(arr) - 1
    # [0, 1, 2, 3, 4]

    while min <= max:
        middle = min + max
        if arr[middle] == target:
            return middle
        if arr[middle] > target:
            max = middle - 1
        else:
            min = middle + 1


    return -1  # not found
