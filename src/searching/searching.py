def linear_search(arr, target):
    if len(arr) == 0:
        return -1

    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1

    indices = {'left': 0, 'right': len(arr) - 1, 'mid': (len(arr)-1)//2}
    if indices['mid'] == target:
        return indices['mid']
    
    while (indices['mid'] != target) and (indices['left'] != indices['right']):
        print(f"left:{indices['left']} right: {indices['right']} mid: {indices['mid']} target: {target}")
        if target == arr[indices['mid']]:
            return indices['mid']
        elif target < arr[indices['mid']]:
            indices['right'] = indices['mid']
            indices['mid'] = (indices['left'] + indices['right']) // 2
        elif target > arr[indices['mid']]:
            indices['left'] = indices['mid']
            indices['mid'] = (indices['left'] + indices['right']) // 2 

    return -1  # not found
