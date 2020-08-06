from math import floor


def linear_search(arr, target):
    # Your code here
    
    for i in range (0,len(arr)):
        if target == i:
            return i
    
      


    return -1   # not found

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

 
 # Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr)-1
    while low <= high:
        middle  = floor((low+high)//2)
        if arr[middle]< target:
           low = middle -1
        elif arr[middle]> target:
            high = middle -1   
        else:
            return middle

    return -1  # not found


bsearch = [2,4,6,8,12,13,14]

thing = binary_search(bsearch, 14)
print('thing',thing)