def linear_search(arr, target):
    # Your code here

    if target in arr:
        return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr)-1

    while left < right:
        middle = (left + right) // 2
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        if arr[middle] == target:
            return middle
        if arr[middle] > target:
            right = middle
        else:
            left = middle

    return -1  # not found
