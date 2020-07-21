# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # while loop on flag
    sorting = True
    # track how many items have been sorted
    sorted = -1
    # recursive loop until nothing left to sort
    while sorting:
        # while loop off flag - ends the recursion when sorting is no longer true
        sorting = False
        # increments sorted each time it runs
        sorted += 1
        # index 0 is presumed sorted as it becomes our first compare / swap
        # so our loop starts at index 1
        # -sorted to not loop through what has already been sorted
        for i in range(1, len(arr)-sorted):
            # when a smaller value is found
            if arr[i] < arr[i - 1]:
                sorting = True
                # swap
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

    # end of loop return
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
    # Your code here

    return arr
