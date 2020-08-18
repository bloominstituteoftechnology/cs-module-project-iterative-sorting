def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1

    left = 0
    right = len(arr)
    while left <= right:
        mid = int(left + (right - 1) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found
