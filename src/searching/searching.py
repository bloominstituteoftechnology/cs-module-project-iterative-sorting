def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] is target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = (len(arr) - 1)
    found = -1
    while first <= last and found != 1:
        middle = (first + last) // 2
        if arr[middle] == target:
            found = 1
            return middle
        else:
            # left case
            if target < arr[middle]:
                last = middle - 1
            else:
                # right case
                # search the upper half
                first = middle + 1
    return found  # not found
