def linear_search(arr, target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #find the middle index  of the list
    low = 0
    high = len(arr)-1
    
    #if  target is the middle value then return 1
    while low <= high:
        mid = (low + high)//2
        if target == arr[mid]:
            return mid
        #if target is less than middle value
        #reassign  right most index to point to the element before the midpoint
        if target < arr[mid]:
            high = mid -1
        #if target is greater than middle value
        #reassign leftmost indext to point to the element past to the midpoint
        if target > arr[mid]:
            low = mid + 1
    return -1  # not found

arr1 = [-2, 7, 3, -9,-8, 5, 1, 0, 4, -6]
print(binary_search(arr1, -3))