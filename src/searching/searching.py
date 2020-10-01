def linear_search(arr, target):
    # Your code here
    #$Search for Target In Array$#
    for i in range(len(arr)):
        #$ Target is present then return element$#
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    #$ SET a START and END and Found Variable In Order to Make Mini Search Fields$#
    start = 0
    end = (len(arr)-1)
    #$ AS Long as START is Not Equal to END and END is GREATER$#
    while start <= end:
        #$find the middle element then first to make sure the middle is not the target$#
        middle = (start + end)//2
        if arr[middle]== target:
            return middle
            #$ if the target is smaller then middle make a left case else make a right case$#
        else:
            if target < arr[middle]:
                end = middle + 1
            else:
                start = middle - 1
    return -1 #not found




