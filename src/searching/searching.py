def linear_search(arr, target):
    for x in range(0, len(arr)):
        if arr[x] == target:
            return x

    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr)

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle

        if target < arr[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return -1
