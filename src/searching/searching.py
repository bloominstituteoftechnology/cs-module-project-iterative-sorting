def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    # If not found, return -1
    return -1

def binary_search(arr, target):
    # Set pointers for low and high in each range, start with full array
    low = 0
    high = len(arr) - 1

    # While low <= high loop through elements
    while low <= high:
        # Find middle of the current range
        mid = (low + high) // 2
        # Set pointer to middle
        guess = arr[mid]

        if guess == target:
            return mid

        # If target is smaller than the middle, eliminate the top half of the arr
        if guess > target:
            high = mid - 1
        # If target is larger than the middle, elimiate the bottom half of the arr
        else:
            low = mid + 1

    # If not found, return -1
    return -1
