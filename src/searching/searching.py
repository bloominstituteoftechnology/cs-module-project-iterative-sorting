def linear_search(arr, target):
    # Your code here
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    mini = 0
    med = 0
    high = len(arr) -1
    while mini <= high:
        med = mini + high //2
        if arr[med] == target:
            return med
        elif arr[med] > target:
            high = med - 1
        else:
            mini = med + 1

    # Your code here
    return -1  # not found
