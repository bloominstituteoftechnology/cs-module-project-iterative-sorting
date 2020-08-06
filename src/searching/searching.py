def linear_search(arr, target):
    for index, elem in enumerate(arr):
        if elem == target:
            return index

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    first = 0
    last = len(arr) - 1

    while first <= last:
        middle = (first + last) // 2
    
        if arr[middle] == target:
            return middle
        else:
            if arr[middle] > target:
                last = middle - 1
            else:
                first = middle + 1

    return -1  # not found
