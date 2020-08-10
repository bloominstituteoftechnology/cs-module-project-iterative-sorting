# TO-DO: Complete the selection_sort() function below
def selection_sort(arr): # O(n^2)
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        boundary = i
        smallest_index = boundary
        smallest_value = arr[boundary]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(boundary, len(arr)):# O(n)
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr): # O(n^2) worst case, O(n) if array is sorted
    # Your code here
    swaps_occured = True

    while swaps_occured:
        swaps_occured = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occured = True

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
