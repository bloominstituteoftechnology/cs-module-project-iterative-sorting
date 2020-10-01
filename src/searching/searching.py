def linear_search(arr, target):
    # for item in the range of the length of the array
    for i in range(0, len(arr)):
        # if the value is equal to the target
        if arr[i] == target:
            # return the array's index
            return i
    # if not found 
    return -1



# Write an iterative implementation of Binary Search
def binary_search(arr, target, low, high):
     # if empty array
    if len(arr) == 0:
        return -1
    # if no high value has been set
    if high == None:
        # the high index is the length of the array - 1
        high = len(arr) - 1
    # create the midpoint 
    midpoint = (high + low) // 2
    # if the midpoint value is the target
    if arr[midpoint] == target:
        return midpoint
    # if the midpoint value is less than the target
    elif arr[midpoint] < target: 
        # set a new low 
        low = midpoint + 1
        # then run through again
        return binary_search(arr, target, low, high)
    # if the midpoint value is mire than the target
    elif arr[midpoint] > target:
        # set a new high 
        high = midpoint - 1 
        # then run through again
        return binary_search(arr, target, low, high)
    # if the midpoint value is none of these
    else:
        return -1  # not found
