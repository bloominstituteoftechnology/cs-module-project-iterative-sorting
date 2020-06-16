def linear_search(arr, target):
    # get index and value and interate through entire array
    for i, value in enumerate(arr):
        # if the value equals the target
        if value == target:
            # return the value's index position
            return i
    
    return -1   # not found


# array = [2, 4, 6, 23, 66, 34, 12]
# print(linear_search(array, 23))


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # start with low index at 0
    low_index = 0
    # and high index at the last index in the array
    high_index = len(arr) - 1
    
    while low_index <= high_index:
        
        # add low and high index, divide, and round down to get the middle
        #. index. Will serve as our guess guess
        middle_index = (low_index + high_index) // 2
        
        # if this guess is equal to the target, return the target's index
        if target == arr[middle_index]:
            return middle_index
        
        # if the target is less than the guess, for the next loop we can make
        #. the high index one less than the last middle
        if target < arr[middle_index]:
            high_index = middle_index - 1
            
        # if the target is more, for the next loop we can make the low index
        #. one more than the last middle
        if target > arr[middle_index]:
            low_index = middle_index + 1
        

    return -1  # not found

# array2 = [5, 34, 43, 45, 123, 843]
# print(binary_search(array2, 5))
