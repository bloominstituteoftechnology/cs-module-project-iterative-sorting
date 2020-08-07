def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # We start with the first element and we end with the last element
    begin_index = 0
    # We put -1 because Python starts the indexing position at 0
    end_index = len(arr) - 1

    # as long as "begin_index" value is lower than "end_index"
    while begin_index <= end_index:
        # the midpoint should be the middle position between our "begin_index" and the rest of the values
        midpoint = begin_index + (end_index - begin_index) // 2
        # this will return the value instead of the position of our midpoint
        midpoint_value = arr[midpoint]

        # if our target is equal to our midpoint value, return the midpoint
        if midpoint_value == target:
            return midpoint
        
        # The target we're looking for is to the left
        elif target < midpoint_value:
            # the "end_index" is the element to the left of our midpoint
            end_index = midpoint - 1

        # else if the target is greater than the midpoint
        else:
            # We only need to check the "target" to the right of the midpoint by repositioning our "begin_index"
            begin_index = midpoint + 1

    return -1  # not found