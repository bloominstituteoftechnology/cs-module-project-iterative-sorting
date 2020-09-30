
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # or True

    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    min = 0
    max = (len(arr) - 1)
    found = False

    while min <= max and not found:
        # find the middle of the array
        middle = ((max + min) // 2)
        if arr[middle] == target:
            found = True
        elif target < arr[middle]:
            max = middle - 1
        elif target > arr[middle]:
            min = middle + 1

    return found
