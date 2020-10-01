def linear_search(arr, target):
    # Your code here
	for i in range(0, len(arr)):
		if arr[i] == target:
			return i
	return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    offset = 0                          # Offset holds amount trimmed from original array's left side
    for i in range(0, len(arr)):
        m = int(len(arr) / 2)           # Calculate middle

        if arr[m] == target:            # Found target in array
            return m+offset             # return index in trimmed array

        if arr[m] > target:             # Compare and trim array
            arr = arr[:m]
        else:
            offset += len(arr[:m])      # Increment offset via what was sliced off the left side of the array
            arr = arr[m:]

    return -1                           # Not found
