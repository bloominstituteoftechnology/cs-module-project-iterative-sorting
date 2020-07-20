def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    ## divide in half
    # if equals, return true
    # if smaller, return left half
    # else return right target
    # if at the end, return false

    left_index = 0
    right_index = len(arr)-1
    # length = len(arr)
    while right_index - left_index > 0:
        mid_index = (left_index + right_index) // 2
        if arr[mid_index] > target:
            right_index = mid_index
        elif arr[mid_index] < target:
            left_index = mid_index
        else:
            return mid_index

    return -1  # not found
