def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    mid = (high + low) // 2
    while high > low:
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # not found
