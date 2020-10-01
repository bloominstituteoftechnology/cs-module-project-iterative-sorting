# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range((i + 1), len(arr)): 
            # why does it have to go all the way to the end. len(arr) - 1 
            # #wasn't iterating the last element of the array

            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
        
    print(arr)
    return arr
    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swap = True
    while swap:
        #will switch to True if a swap is performed
        swap = False

        # 1. Loop through your array, but not the last element
        for i in range(0, len(arr) - 1):
            # Compare each element to its neighbor
            if arr[i + 1] < arr[i]:
                # If elements in wrong position (relative to each other, swap them)
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap = True

    print(arr)
    return arr

'''
STRETCH: implement the Counting Sort function below

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
def counting_sort(arr, maximum=None):
    # get max number for size of array
    maximum = largest_number(arr)

    # create an array the size of the largest number + 1
    counts = [0] * (maximum + 1)
    # Count the number of times each value appears.
    for item in arr:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:    
            counts[item] += 1

    # Overwrite counts to hold the next index an item with
    # a given value goes. So, counts[4] will now store the index
    # where the next 4 goes, not the number of 4's our
    # list has.
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(arr)

    # Run through the input list
    for item in arr:
        
        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1

    return sorted_list

def largest_number(arr):
    max_number = 0
    for i in range(0, len(arr) - 1):
        if arr[i] > max_number:
            max_number = arr[i]
    
    return max_number
