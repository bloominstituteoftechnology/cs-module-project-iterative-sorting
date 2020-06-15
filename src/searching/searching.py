def linear_search(arr, target):
    # Loop through each element
        # If the element is equal to the target, return the index

    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Set low to 0
    # Set high to len(arr) - 1
    # While the low index is less than or equal to the high index
        # Get mid through adding low and high and dividing by 2 using //
        # If mid matches, return mid index
        # else if target less than mid, look in low through mid - 1
        # else if target is greater than mid, look in mid + 1 through high

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + high // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found
