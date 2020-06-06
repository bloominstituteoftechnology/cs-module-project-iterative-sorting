def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    current_array = arr
    add_midpoint = 0
    while len(current_array) > 1:
        midpoint = 0
        if (len(current_array) % 2) == 0:
            midpoint = int(len(current_array) / 2)
        else:
            midpoint = int(len(current_array) / 2 + 1)

        if current_array[midpoint] == target:
            return add_midpoint + midpoint
        elif target < current_array[midpoint]:
            current_array = current_array[:midpoint]
        else:
            add_midpoint = midpoint + add_midpoint
            current_array = current_array[midpoint:]

    if len(current_array) == 1:
        if current_array[0] == target:
            return 0

    return -1  # not found
