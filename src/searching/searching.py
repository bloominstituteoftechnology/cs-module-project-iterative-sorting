def linear_search(arr, target):

    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    top = len(arr)-1
    bottom = 0

    while top >= bottom:
        middle = (top + bottom) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] > target:
            high = middle - 1

        else:
            low = middle + 1

    return -1  # not found
