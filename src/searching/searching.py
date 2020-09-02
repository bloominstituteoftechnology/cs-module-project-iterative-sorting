def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if target == arr[i]:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    size_of_list = len(arr) - 1
    # Your code here
    first_element = 0
    last_element = size_of_list

    while first_element <= last_element:
        mid_point = (first_element + last_element) // 2
        if arr[mid_point] == target:
            return mid_point

        if target > arr[mid_point]:
            first_element = mid_point + 1

        else:
            last_element = mid_point - 1

        if first_element > last_element:
            return None

    
    return -1  # not found
