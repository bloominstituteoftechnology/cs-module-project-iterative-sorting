def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    min = 0
    max = len(arr) - 1
    
    while min <= max:
        mid = (max + min) // 2
        
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            max = mid - 1
        elif target > arr[mid]:
            min = mid + 1
            
    


    return -1  # not found
