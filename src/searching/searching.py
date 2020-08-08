def linear_search(arr, target):
    # Your code here
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) -1

    while True and not start > end:
        middle_idx = (start + end) // 2
        elem = arr[middle_idx]

        if elem == target:
            return middle_idx
        elif elem > target:
            end = middle_idx - 1
        else:
            start = middle_idx + 1

    return -1  # not found
