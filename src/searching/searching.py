def linear_search(arr, target):
    print(f"taget: {target} ")
    # Your code here
    # if target in arr:
    #     print(f"target: {target} ")
    #     return arr.index(target)

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    arr.sort()

    while low <= high:
        print(f"low: {low} high: {high} ")
        mid = (low+high) // 2
        print(f"mid: {mid} ")
        if arr[mid] == target:
            globals()['pos'] = mid
            return mid
        else:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return -1

    # Your code here
    # while low >= 0:
    #     mid = (high + low)//2
    #     print(f"mid: {mid} ")

    #     if arr[mid] == target:
    #         return mid
    #     elif arr[mid] > target:
    #         print(f"target: {target} ")
    #         # high = mid - 1
    #         # return binary_search(arr, target)
    #         for i in range(0, mid):
    #             if arr[i] == target:
    #                 return i
    #     elif arr[mid] < target:
    #         # low: mid + 1
    #         # return binary_search(arr, target)
    #         for i in range(mid + 1, len(arr)):
    #             if arr[i] == target:
    #                 return i
    #     else:
    #         return -1  # not found


# Testing
arr1 = [9, 10, 2, 55, 70]
# print(linear_search(arr1, 3))
print(binary_search(arr1, 10))
