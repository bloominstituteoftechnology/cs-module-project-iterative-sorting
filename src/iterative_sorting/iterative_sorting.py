# TO-DO: Complete the selection_sort() function below

'''
1. Start with current index = 0

2. For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side
    of current index and find the smallest element

    b. Swap the element at current index with the
    smallest element found in above loop

'''


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_valued_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            unsorted_element = j
            if arr[unsorted_element] < arr[smallest_valued_index]:
                smallest_valued_index = unsorted_element
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_valued_index] = arr[smallest_valued_index], arr[cur_index]

    return arr


'''
1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
'''

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    # for every element
    # compare that element to it's right ( + 1)
    # if it is greater, swap right to left's place
    # until we have no more swaps
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
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


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
