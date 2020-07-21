def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] is target:
            return index
    return -1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #gaurd for empty array
    if len(arr) == 0:
        return -1
    #gaurd for value out of range
    if target < arr[0] or target > arr[len(arr)-1]:
#        isFinished = True
        return -1
        
    isFinished = False
    slice = arr
    
    while isFinished is False:
                            
#        minIndex = 0
        maxIndex = len(slice) - 1
        midIndex = int(maxIndex / 2)
        midValue = slice[midIndex]
            
        if target > midValue: #greater than
            slice = slice[midIndex+1:]
            continue
            
        if target < midValue: #less than
            slice = slice[:midIndex]
            continue
            
        if target is midValue: #found it!
#            isFinished = True
            return arr.index(target)
        else: #doesn't exist
#            isFinished = True
            return -1 