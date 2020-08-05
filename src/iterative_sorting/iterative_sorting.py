# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index       = i
        smallest_index  = cur_index
        found_smaller   = False

        # Find the smallest value less the current value 
        #   to the right of the current value
        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                found_smaller  = True

        # Swap the current value with a smaller value
        if found_smaller:
            # Found a smaller value "to the right"
            #   of the current value
            tmp_val             = arr[smallest_index]
            arr[smallest_index] = arr[cur_index]        # Set the smallest value to the current value
            arr[cur_index]      = tmp_val               # Set the current value to the smallest value found

    return arr


# Implement the Bubble Sort
def bubble_sort(arr):
    # Flag indicating if a swap has been made
    flg_upd_mde = True

    # Iterate through the array
    while flg_upd_mde:
        flg_upd_mde = False

        for i, elm in enumerate(arr):
            # Are we done with the iteration?
            if i == len(arr) - 1:
                break

            # Is the current element larger the next element?
            if elm > arr[i+1]:
                # Current element is larger the next element, swap the elements
                arr[i]      = arr[i+1]
                arr[i+1]    = elm
                flg_upd_mde = True

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
