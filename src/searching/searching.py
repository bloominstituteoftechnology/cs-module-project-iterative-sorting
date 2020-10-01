def linear_search(arr, target):
    # Your code here
    for item in range(len(arr)):
        if arr[item] == target:
            return item

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        midpoint = start + (end - start) // 2
        mid_item = arr[midpoint]

        if target == mid_item:
            return midpoint
        elif target < mid_item:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return -1  # not found
