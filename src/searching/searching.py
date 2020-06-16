def linear_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1

    index = {"left": 0, "mid": (len(arr) - 1) // 2, "right": len(arr) - 1}
    if index["mid"] == target:
        return index["mid"]

    while (index["mid"] != target) and (index["left"] != index["right"]):
        print(
            f"left:{index['left']} right: {index['right']} mid: {index['mid']} target: {target}"
        )
        if target == arr[index["mid"]]:
            return index["mid"]
        elif target < arr[index["mid"]]:
            index["right"] = index["mid"]
            index["mid"] = (index["left"] + index["right"]) // 2
        elif target > arr[index["mid"]]:
            index["left"] = index["mid"]
            index["mid"] = (index["left"] + index["right"]) // 2

    return -1  # not found

## FROM LECTURE
# def binary_search(arr, target):
#     # Your code here
#     # we're searching in between the low and high indices
#     low = 0
#     high = len(arr) - 1


# ​
#    # loop so long as low hasn't moved passed high
#    while low <= high:
#         mid = (low + high) // 2
# ​
#         # base case where we've found our target
#        if arr[mid] == target:
#             return mid
#         elif target < arr[mid]:
#             # toss out the right side since the target
#             # has to be on the left side
#             # do this by setting high to be mid - 1
#             high = mid - 1
#         else:
#             # toss out the left side since the target
#             # has to be on the right side
#             # do this by setting low to mid + 1
#             low = mid + 1
# ​
#    return -1  # not found
