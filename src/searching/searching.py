def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # why not return None?


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    lo = 0
    hi = len(arr)

    while True:
        mid = round((lo + hi) / 2)
        if hi < lo or mid >= len(arr):
            return -1  # why not return None?
        current = arr[mid]

        if target == current:
            return mid
        elif target < current:
            hi = mid
        else:
            lo = mid + 1


blah = [1, 5, 9, 12, 12, 14, 17, 30, 42, 250, 390, 533]

i = binary_search(blah, 42)
print(i)
