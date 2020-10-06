def linear_search(arr, target):
    # Your code here
    for index, item in enumerate(arr):
        if item is target:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]

        if guess is target:
            return middle
        elif guess > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1  # not found
