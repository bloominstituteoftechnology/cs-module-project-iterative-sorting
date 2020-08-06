def linear_search(arr, target):
    for i in range(len(arr)): #* for i in range of the length of arr
        if arr[i] == target: #* if i is equal to the target
            return i #* return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0 #* set low to zero
    high = len(arr) - 1 #* set high to the length of arr minus 1
    mid = 0 #* set mid to zero

    while low <= high: #* if low is less than or equal to high
        mid = (high + low) // 2 #* mid then equals high + low divided by 2
        
        if arr[mid] < target: #* if mid is less than the target
            low = mid + 1 #* low then equals mid plus one
        
        elif arr[mid] > target: #* if mid is greater than the target
            high = mid - 1 #* high then equas mid minus 1

        else:
            return mid #* return mid


    return -1  # not found

#* ALL TESTS PASSED
