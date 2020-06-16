def linear_search(arr, target):
    """
    Linear search algorithm implementation
    
    Args:
        arr: Array of values to search
        target: The value for which the algorithm is searching

    Returns:
        -1: If target not found in arr
        Index of target in arr: If target found in arr

    Examples:
        >>> arr1 = [0,2,4,6,8,10,12]
        >>> linear_search(arr1, 4)
        3
        >>> linear_search(arr1, 3)
        -1
        
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


def binary_search(arr, target):
    """
    Binary search algorithm implementation
    
    Args:
        arr: Array of values to search
        target: The value for which the algorithm is searching

    Returns:
        -1: If target not found in arr
        Index of target in arr: If target found in arr

    Examples:
        >>> arr1 = [0,2,4,6,8,10,12]
        >>> binary_search(arr1, 4)
        3
        >>> binary_search(arr1, 3)
        -1
        
    """

    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1  # not found
