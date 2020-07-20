def linear_search(arr, target):
    """
    Traverse the dataset one item at a time until either you find the item you are
    looking for OR check every item in the set and verify the item you are
    looking for is not there.
    """
    # Your code here
    for x in range(len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    """
    Returns either the index of the target in the arr
    or, if the target isn't in the arr, return -1
    """
    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:

        # 1. Compare the target element to the midpoint
        mid = (high + low) // 2

        # 2. If the midpoint element matches our target, then we've
        #    we've found what we're looking for, return the midpoint
        #    index
        if target == arr[mid]:
            return mid
        # 3. Determine which half to go in; toss our the other half
            # reassign either left or right index to point to the element
            # past the midpoint
        if target < arr[mid]:
            # cut out the right half
            # reassign high to mid -1
            high = mid - 1
        if target > arr[mid]:
            # cut out the left half
            # reassign low to mid + 1
            low = mid + 1

    return -1  # not found


if __name__ == "__main__":
    my_list = [23, 34, 55, 67]

    # print(linear_search(my_list, 2))

    arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
    print(linear_search(arr1, 7))
    # breakpoint()
