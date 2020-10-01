def linear_search(arr, target):
    # Your code here
    for item in arr:
        if item == target:
            return arr.index(item)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # pointers
    low = 0 
    high = len(arr) -1

    #loop continues while low pointer is less than or equal to the high pointer
    while low <= high:
        #average low and high by adding together, dividing by 2 and rounding down
        middle = (low + high) //2 
        guess = arr[middle]
        
        #if guess is correct
        if guess == target:
            return arr.index(guess)
        #if guess is high
        if guess > target:
            high = middle -1
        #if guess is low
        else:
            low = middle +1
    

    return -1  # not found
