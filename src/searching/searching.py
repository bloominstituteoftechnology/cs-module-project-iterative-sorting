def linear_search(arr, target):
    # Your code here
    for i, n in enumerate(arr):
        if n == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (h + l) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            h = m
    return -1  # not found
