def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = array[middle]
        if guess == target:
            return middle

        if guess > target:
            high = middle - 1

        else:
            low = middle + 1

    return None
