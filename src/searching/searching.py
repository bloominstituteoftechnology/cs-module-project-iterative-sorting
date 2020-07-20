def linear_search(arr, target):
    # Your code here
    # go through each item in the list, one at a time
    # if the item is not the target, return false
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # compare search target to middle of the list
    # if the target is bigger than the value of the middle of the 
    # list, eliminate the smaller half and repeat for the remaining 
    # middle, repeat process until number is found or if the number 
    # cannot be found

    # declare min and max parameters
    min_value = 0
    max_value = len(arr) - 1
    
    # start loop
    while min_value <= max_value:
        mid = (max_value + min_value) // 2
        if target < arr[mid]:
            max_value = mid - 1
        elif target > arr[mid]:
            min_value = mid + 1
        else:
            return mid

    return -1  # not found
