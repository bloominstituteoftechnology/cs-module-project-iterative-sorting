def linear_search(arr, target):
    # Your code here
    for x in range(0, len(arr)):
        if target == arr[x]:
            print(f"target found in list at index {x}.")
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search

def binary_search(arr, target, start = None, end = None):
    if start is None and end is None:
        start = 0
        end = len(arr) - 1
    # Your code here
    if start > end:
        return -1
    else:
        mid = (start + end) // 2

        if arr[mid] == target: 
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)