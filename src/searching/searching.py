def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        midpoint = start + (end - start) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == target:
            return midpoint
        elif target < midpoint_value:
            end = midpoint - 1
        else:
            start = midpoint + 1


    return -1  # not found
