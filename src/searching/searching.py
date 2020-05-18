def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set the outter bounds
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # is your mid the target?
        if arr[mid] == target:
            return mid
        
        
        if arr[mid] < target:
            left = mid + 1

        else: right = mid - 1


    return -1  # not found
