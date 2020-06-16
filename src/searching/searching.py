def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] is target:
            return i

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target, last= 0):

    # Your code here
    index_count = len(arr)
    if index_count >= 1:
        half = index_count // 2
        if arr[half] is target:
            return half + last
        elif arr[half] < target:
            arr_range = index_count - half
            index = last + arr_range
            return binary_search(arr[arr_range:], target, index)
        else:
            arr_range = 0 + half
            index = last + arr_range
            return binary_search(arr[0: arr_range], target, index - half)
    else:
        return -1  # not found
