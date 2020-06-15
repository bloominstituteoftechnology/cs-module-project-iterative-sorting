def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # initialize low and high
    low_idx = 0
    high_idx = len(arr) - 1
    while low_idx < high_idx:
        # get index between the low and high
        mid_idx = int((low_idx + high_idx) / 2)
        # check if middle is the target
        if arr[mid_idx] == target:
            return mid_idx
        # update low and high based on whether
        # it was too low or high
        if arr[mid_idx] < target:
            low_idx = mid_idx
        else:
            high_idx = mid_idx

    return -1  # not found
