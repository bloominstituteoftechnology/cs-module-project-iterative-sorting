"""
Iterative search assignment.
"""

def linear_search(arr, target):
    """
    A straightforward linear search, left-to-right.
    """
    for index, item in enumerate(arr):
        if item == target:
            return index

    return -1   # not found


def binary_search(arr, target):
    """
    An iterative implementation of binary search.
    """
    if len(arr) == 0:
        return -1 # array empty

    low = 0
    high = len(arr)

    while high > low:
        mid = (low + high) // 2
        if arr[mid] == target:
            # Found.
            return mid

        if arr[mid] > target:
            # Too high, search lower half.
            high = mid

        elif arr[mid] < target:
            # Too low, search upper half.
            low = mid + 1

    return -1  # not found
