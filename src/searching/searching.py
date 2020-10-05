def linear_search(arr, target):
    # Your code here
    ## SEARCH TARGET IN ARRAY
    for i in range(len(arr)):
        ## RETURN ELEMENT ONCE THE TARGET IS PRESENT
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    ## FIND A VAR IN ORDER TO CREATE MINI SEARCH FIELDS
    start = 0
    end = (len(arr)-1)
    ## CHECKING TO SEE WHAT IS GREATER 
    while start <= end:
        ## CHECKING TO SEE TARGET IS CORRECT
        middle = (start + end)//2
        if arr[middle]== target:
            return middle
        else:
            if target < arr[middle]:
                end = middle + 1
            else:
                start = middle - 1
    return -1 #not found