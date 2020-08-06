def linear_search(arr, target):
    # Iterate through the array and determine if the 
    #   target has been found
    for i, elm in enumerate(arr):
        if target == elm:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # sub_search is a function searches for a target value
    #   within an array
    def sub_search(target, arr, i_strt, i_end):
        # Are we at the last element to check?
        if i_strt == i_end:
            # Last element to check, have we found our value?
            if target == arr[i_strt]:
                return i_strt
            else:
                return -1
        else:
            # More than one element to check, determine midpoint of the array slice
            idx = i_strt + ((i_strt + i_end) // 2)

            # Do we find the target at midpoint index?
            if target == arr[idx]:
                return idx
            elif target < arr[idx]:
                # Invoke sub_search on the "left" sub slice of the array
                return sub_search(target, arr, i_strt, idx-1)
            else:
                # Invoke sub_search on the "right" sub slice of the array
                return sub_search(target, arr, idx+1, i_end)

    # Validate inbound parameters
    if len(arr) == 0 or target == None:
        # Empty array or missing target, nothing to search
        return -1
    
    # Sort the passed array of values
    arr.sort()

    # Call the sub_search function
    return sub_search(target, arr, 0, len(arr)-1)
    
