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

    low = 0
    mid = len(arr) // 2
    high = len(arr) - 1

    while low <= mid and high >= mid:
        # for i in range(len(arr)):
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # eliminate the right side
            high = mid - 1
            if arr[high] == target:
                return high
        elif arr[mid] < target:
            # eliminate the left side
            low = mid + 1
            if arr[low] == target:
                return low

        mid = (high - low) // 2

    return -1  # not found
