def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        

    return -1  # not found
