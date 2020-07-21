def linear_search(arr, target):
    for index, i in enumerate(arr):
        if target == i:
            return index


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < target: #Target is higher than our checked value, set new low value.
            low = mid + 1
        elif arr[mid] > target:#Target is lower than our checked value, set new high value.
            high = mid - 1
        else: #Target is equal to arr[mid], return mid.
            return mid
    return -1  # not found
