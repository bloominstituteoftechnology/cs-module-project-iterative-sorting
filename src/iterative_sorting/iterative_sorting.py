# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        for j in range(cur_index + 1, len(arr)): # start at next element
            if arr[j] < arr[smallest_index]: # if smaller,
                smallest_index = j # mark as smallest_index

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    
    pass_num = 1 # Keep track of the pass number to not check the elements that have already bubbled up

    while pass_num < len(arr): 
        did_swap = False

        for i in range(len(arr) - pass_num): # Loop through all the elements minus the pass number
            if arr[i] > arr[i + 1]: # if the next element is larger,
                arr[i], arr[i + 1] = arr[i + 1], arr[i] # then swap
                did_swap = True # Make note if we did at least one swap
        
        if not did_swap: # If we didn't do any swaps, the array is ordered
            break # This lets us exit early if we are already sorted

        pass_num += 1

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=None):
    # Initialize buckets
    # Loop through values
        # Place each value in bucket by incrementing that index
    # Construct array from our buckets
    # First pass solution: Loop through buckets, adding the appropriate number of values to our result array
    # Second pass: overwrite data in the arr passed in by looping through the buckets and the occurences

    # If no maximum is passed in, let's find the maximum

    if not maximum:
        maximum = 0
        for value in arr:
            if value > maximum:
                maximum = value

    buckets = [0] * (maximum + 1) # allocate appropriate number of buckets
    
    for value in arr:
        if value < 0: # make sure to guard against negative integers
            return "Error, negative numbers not allowed in Count Sort"
        buckets[value] += 1

    index = 0

    for value, occurences in enumerate(buckets): # bucket index is the value, the int in the bucket is the number of occurences
        for _ in range(occurences): 
            arr[index] = value # overwrite input array with value
            index += 1 # increment index

    return arr

