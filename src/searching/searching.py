def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(array, targetValue):
#Let min = 0 and max=n−1.
#If max<min, then stop; target is not present in array. Return -1.
#Compute guess as the average of max and min, rounded down so that it is an integer.
#If array[guess] equals target, then stop. You found it! Return guess.
#If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
#Otherwise, the guess was too high. Set max = guess - 1.
#Go back to step two.
# Your code here
    min = 0
    max = len(array) - 1
    
    while True:
        if max < min:
            return -1
			
        guess = (max + min) // 2
        middle = array[guess]
        if middle == targetValue:
            return guess
        elif middle < targetValue:
            min = guess + 1
        else:
            max = guess - 1

  