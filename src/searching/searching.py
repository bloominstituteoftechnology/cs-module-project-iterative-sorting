def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        print(range(len(arr)))
        print(f"{i} -- {arr[i]}")
        # print(f"LOOPED {i} TARGET {target}")
        if arr[i] == target:
            return i

    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]

        if guess == target:
            return middle

        elif guess > target:
            high = middle - 1

        else:
            low = middle + 1

    return -1  # not found
