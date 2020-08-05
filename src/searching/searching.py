def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here

    lhi = 0 #left hand index
    rhi = len(arr) - 1 #right hand index

    while lhi <= rhi:
        mid = (lhi + rhi) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lhi = mid + 1
        else:
            rhi = mid - 1

    return -1  # not found
