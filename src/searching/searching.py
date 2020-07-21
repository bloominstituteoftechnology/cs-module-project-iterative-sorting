def linear_search(arr, target):
    for n in range(len(arr)):
        if arr[n] == target:
            return n
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    current_arr = arr
    mid_add = 0
    while len(current_arr) > 1:
        midP = 0
        if (len(current_arr) % 2) == 0:
            midP = int(len(current_arr) / 2)
        else:
            midP = int(len(current_arr) / 2 + 1)

            if current_arr[midP] == target:
                return mid_add + midP
            elif target < current_arr[midP]:
                current_arr = current_arr[:midP]
            else:
                mid_add = midP + mid_add
                current_arr = current_arr[midP:]

    if len(current_arr) == 1:
        if current_arr[0] == target:
            return 0


    return -1  # not found
