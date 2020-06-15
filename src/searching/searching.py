def linear_search(arr, target):
    for index, value in enumerate(arr):
        print(index, value)
        if value == target:
            return index


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
            
        else: 
            right = mid - 1
      


    return -1  # not found