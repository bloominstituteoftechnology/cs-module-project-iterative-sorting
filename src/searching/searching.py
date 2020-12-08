def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        if arr[index] == target:
            return index    # Or return whatever they ask for. The .index() might increase time complexity
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        if guess > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1

    # This didn't work
    # left_index = 0
    # right_index = len(arr) - 1
    # # Want to see if target is greater or less than the midpoint
    # while right_index - left_index < 1:
    #     midpoint = right_index // 2
    #     print(midpoint)
    #     if target == arr[midpoint]:
    #         return midpoint
    #     elif target > arr[midpoint]:
    #         left_index = midpoint
    #     else:
    #         right_index = midpoint

    return -1  # not found
