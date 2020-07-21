def linear_search(array, target):
    """
    Searches for the input target value using linear (sequential) search.
    Returns index if found, otherwise returns -1.
    """
    # Check every element in the array:
    for index in range(len(array)):
        # If found, return the first index that contains the target value:
        if array[index] == target:
            return index
    # If not found, return -1:
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(sorted_array, target):
    """
    Searches an already-sorted array/iterable for the input target value 
    using binary search. Returns index if found, otherwise returns -1.
    """
    first = 0
    last = len(sorted_array) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if sorted_array[midpoint] == target:
            return midpoint
        elif sorted_array[midpoint] > target:
            last = midpoint - 1
        elif sorted_array[midpoint] < target:
            first = midpoint + 1
        
    # If not found, return -1:
    return -1
