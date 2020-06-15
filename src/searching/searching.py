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
