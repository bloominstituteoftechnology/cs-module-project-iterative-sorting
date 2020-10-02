def linear_search(arr, target):
    # Your code here
    for i, v in enumerate(arr):
        if v == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1

    z = 0
    x = len(arr) - 1

    if arr[z] > target or arr[x] < target:
        return -1

    if arr[z] == target:
        return z
    elif arr[x] == target:
        return x

    while x - z >= 2:
        mid = (z + x) // 2
        if arr[mid] > target:
            x = mid
        elif arr[mid] < target:
            z = mid
        else:
            return mid
    return -1  # not found
