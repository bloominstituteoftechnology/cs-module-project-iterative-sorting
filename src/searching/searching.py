def linear_search(arr, target):
    # Your code here
    # for loop to iterate through index to match the target value
    # return the index
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr)-1

    for i in range(0, len(arr)):

        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            end = middle - 1
        elif arr[middle] < target:
            start = middle + 1
    return -1 # not found