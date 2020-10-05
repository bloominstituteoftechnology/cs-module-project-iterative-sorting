def linear_search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return 1


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    last = len(arr)-1
    index = -1

    while first <= last and index <0:
        middle = (first + last) // 2

        if target == arr[middle]:
            index = middle
        else:
            if target < arr[middle]:
                last = middle - 1
            else:
                first = middle - 1 


    return index  
