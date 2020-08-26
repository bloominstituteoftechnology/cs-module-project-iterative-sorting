def linear_search(arr, target):
    for num in range(len(arr)):
        if arr[num] == target:
            # print("its in position", arr[num])
            return num
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # * find middle point (index)    = (start + end)/2
    # * compare the value in the middle with target
    # * shrinking and modifying arays are not very efficient

    start = 0
    end = (len(arr)-1)

    found = 0
    while end >= start and not found:
        middle_index = (start + end)//2
        # * compare the value in the middle with the target
        # * check  if middle val is the same as target, set found to True
        if arr[middle_index] == target:
            found += 1
        # * move start or end index closer to one another, and shrink our search space
        else:
            if target < arr[middle_index]:
                # * search left hand side
                # * move pointers
                # * end is median - 1 :  the middle is not even your target anyway
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1

    return -1

    # return -1  # not found
