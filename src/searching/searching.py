def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    first = 0
    last = len(arr) - 1
    index = -1 # not found (yet)

    while first <= last and index < 0:
        middle = (first + last) // 2

        if arr[middle] == target:
            index = middle
        else:
            if target < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return index
