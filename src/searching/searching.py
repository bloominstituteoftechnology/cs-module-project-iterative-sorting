def linear_search(arr, target):
    for item in arr:
        if item == target:
            return arr.index(item)


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Check if target is present at mid
        if arr[mid] < target:
            low = mid + 1
        # If target is greater, ignore left half
        elif arr[mid] > target:
            high = mid - 1
        # If target is smaller, ignore right half
        else:
            return mid


    return -1  # not found
