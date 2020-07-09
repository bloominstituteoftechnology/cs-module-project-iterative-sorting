def linear_search(arr, target):
    # Your code here
    for item in range(len(arr)):
        if arr[item] == target:
            return item        
    return -1   # not found

print(linear_search([6,3,5,9,8,2],0))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    first = 0
    last = len(arr)-1

    while first <= last:
        mid = first + (last - first) // 2
        mid_item = arr[mid]

        if target == mid_item:
            return mid
        elif target < mid_item:
            last = mid -1 
        else: 
            first = mid + 1       

    return -1  # not found

print(binary_search([2,5,7,8,9,11,14,16],4))