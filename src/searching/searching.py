def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    min = 0
    max = len(arr) -1
    middle =0
    while min <= max:
        middle = (min + max) //2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            max = middle -1
        elif target > arr[middle]:
            min = middle +1
        else:
            return middle
    return -1                 
    # return False  # not found
arr1 = [2, 7, 3, 9, 5, 1, 0, 4, 6]
print('LS, Targeted value Located at index: ',linear_search(arr1, 0))

print('BS, Targeted value Located at index: ',binary_search(arr1, 7))