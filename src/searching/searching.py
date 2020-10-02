def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i]==target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start_i=0
    end_i=len(arr)-1

    while start_i<=end_i:
        mid=(start_i+end_i)//2
        if arr[mid]==target:
           return mid
        if arr[mid]<target:
            start_i=mid+1
        else:
            end_i=mid-1


    # Your code here


    return -1  # not found
