
def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    end = len(arr)
    start = 0

    while end > start:
        middle = (end + start) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            end = middle
        elif target > arr[middle]:
            start = middle


    return -1  # not found


# Flexed Code ---------------------------------------------

# def linear_search(arr, target):
#     # Your code here
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return 1

#     return -1   # not found


# # Write an iterative implementation of Binary Search
# def binary_search(arr, target):

#     # Your code here
#     first = 0
#     last = (len(arr) - 1)
#     found = -1

#     while first <= last and not found:

#         middle = (first + last) // 2

#         if arr[middle] == target:
#             found = 1

#         else:
#             if target < arr[middle]:
#                 last = middle -1
#             else:
#                 first = middle + 1

#     return -1  # not found