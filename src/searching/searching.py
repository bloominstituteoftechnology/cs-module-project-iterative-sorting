# def linear_search(arr, target):
#     # Your code here
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i

#     return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    first = 0
    last = len(arr) - 1
    mid = 0
    
    while first <= last:
        
        mid = (first + last) // 2
        
        if arr[mid] < target:
            last = mid + 1
            
        elif arr[mid] > target:
            last = mid - 1
            
        else:
            return mid
            
    return -1

# Test data
arr = [2, 4, 8, 12, 21, 10, 7]
target = 10

result = binary_search(arr, target)

if result != -1:
    print("Element is present at index {0}".format(result))
else:
    print("Element is not present at index {0}".format(result))
    
    