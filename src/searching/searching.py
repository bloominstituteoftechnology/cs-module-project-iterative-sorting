def linear_search(arr, target):
    for x in range(0, len(arr)):
        if arr[x] == target:
            return x
    return -1



def binary_search(arr, target):
    start = 0
    end = len(arr)

    if end == 0:
        return -1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        if target < arr[middle]:
            end = mid - 1

        else:
            start = mid + 1
    return -1
