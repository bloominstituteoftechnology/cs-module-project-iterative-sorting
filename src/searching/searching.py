def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            # found
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:

        middle = (first + last) // 2

        if arr[middle] == target:
            # return index of target not the value
            return middle
        else:
            if target < arr[middle]:
                # if target is less than the value of the mid element, make the element before the middle the last element to search through
                last = middle - 1
            else:
                # if the target is greater than the middle element, make one after the middle element the starting point for the next search
                first = middle + 1
    # Same as returning false

    return -1  # not found
