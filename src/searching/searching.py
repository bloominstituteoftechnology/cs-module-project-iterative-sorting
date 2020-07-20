def linear_search(arr, target):

    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1  


def binary_search(arr, value):
    first = 0
    last = (len(arr) - 1)
​
    found = -1
​
    while first <= last and found = -1:
        # find middle using integer divsion
        middle = (first + last) // 2
​
        if arr[middle] == value:
            found = middle
​
        else:
            if value < arr[middle]:
                # search lower half of remainder
                last = middle - 1
            else:
                # search upper half of remainder
                first = middle + 1
​
    return found

