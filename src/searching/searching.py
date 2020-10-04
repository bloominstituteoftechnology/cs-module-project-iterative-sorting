def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0 
    end = len(arr)-1

    while end >= start: 
        # get to the middle
        mid_index = (start+end) // 2 
        #compare value of mid index to target
        # if mid index value is equal to target return mid index 
        if arr[mid_index] == target:
            return mid_index
        else: 
            # move start or end index so search space is reduced by half
            if target < arr[mid_index]:
                end = mid_index-1
            else: 
                start = mid_index+1
                
    return -1  # not found
