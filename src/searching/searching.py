def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found
A = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
target = -8
#print(linear_search(A, target))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # pairs = {}
    # for i in range(len(arr)):
    #     pairs[arr[i]] = i
    # print(pairs)
        
    #sort arr
    # arr.sort()
    # print(arr)
    mid = (len(arr)-1)//2
    print('mid', mid)
    # Your code here
    count = 0
    while count < mid/2:
        print(arr[mid])
        if arr[mid] == target:
            return mid 
        elif arr[mid + 1] == target:
            return mid+1
        elif arr[mid-1] == target:
            return mid-1
        elif target > arr[mid]:
            if mid == 1:
                print 
                mid == 2
            else:
                mid = mid + mid//2
            print('> mid', mid)
            # arr = arr[mid+1: len(arr)]
            # mid = (len(arr)-1)//2
        elif target < arr[mid]:
            #arr = arr[0: mid-1] 
            mid = mid//2
        print(arr)
    return -1

A = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
target = -6
print(binary_search(A, target))