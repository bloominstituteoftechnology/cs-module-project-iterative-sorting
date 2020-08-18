def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = round((start + end) // 2)
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

    return -1  # not found
