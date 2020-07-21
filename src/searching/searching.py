def linear_search(arr, target):
    for x in range(len(arr)):
    	if arr[x] == target:
    		return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
	minimum = 0
	maximum = (len(arr)-1)

	while minimum <= maximum:
		mid = minimum + (maximum - 1)

		if arr[mid] == target:
			return mid

		elif arr[mid] < target: # Ignore left half
			minimum = mid + 1

		else: # Ignore right half
			maximum = mid - 1

	return -1

