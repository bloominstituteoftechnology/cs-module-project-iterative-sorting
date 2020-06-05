def linear_search(arr, target):
    for i in range (0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # arr = arr.sort() #have to guarantee that the items are sorted
    top  = max(0, len(arr) - 1) #highest index we're looking at
    bottom = 0 #lowest index we're looking at
    window = len(arr[bottom:top]) # the window of indices that we are looking at
    mid = int(window / 2) # choose a mid point
    while top > bottom:
        if arr[mid] == target:
            return mid
        
        elif target > arr[mid]:
            bottom = mid + 1
            window = len(arr[bottom:top])
            mid = int(window / 2)
        
        else:
            top = mid - 1
            window = len(arr[bottom:top])
            mid = int(window / 2)  
            
        if top == bottom:
            if target == arr[top]:
                return top

    return -1  # not found
