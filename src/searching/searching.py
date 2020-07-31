def linear_search(arr, target):
    # Will loop through the list (array) until
    # the target is found will then return the index at 
    # which the target is found or -1 if not found
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    if not arr:
        return -1
    # doing the binary search here
    front = 0
    end = len(arr) -1
    # Will continue to do the while loop util 
    # end is less than front
    while end >= front:
        mid = (end + front)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target: # will need to discard the rhs 
            end = mid -1
        else:
            front = mid +1


    return -1  # not found
