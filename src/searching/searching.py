def linear_search(arr, target):
    # Your code here
    for item in arr:
        if item == target:
            return arr.index(item)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr) - 1)

    while start <= end:
        middle = (start + end) // 2
        check = arr[middle]

        if check == target:
            return arr.index(check)
        if check > target:
            end = middle - 1
        if check < target:
            start = middle + 1

    return -1  # not found
