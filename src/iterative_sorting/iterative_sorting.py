# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        while smallest_index < len(arr) - 1:
            smallest_index += 1
            if arr[cur_index] > arr[smallest_index]:

        # TO-DO: swap
        # Your code here
                smallest_elemet = arr[smallest_index]
                arr[smallest_index] = arr[cur_index]
                arr[cur_index] = smallest_elemet

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    cur_index = 0
    swap = False
    while cur_index < len(arr) - 1:
        neighbor_index = cur_index + 1
        if arr[cur_index] > arr[neighbor_index]:
            neighbor_element = arr[neighbor_index]
            arr[neighbor_index] = arr[cur_index]
            arr[cur_index] = neighbor_element
            swap = True
        # check to see if no swaps were made
        if swap:
            cur_index = 0
            swap = False
        else:
            cur_index += 1

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
    if not arr:
        return arr

    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'

    largest = max(arr) + 1
    elements = [0 for i in range(0, largest)]

    for i in range(0, len(arr)):
        elements[arr[i]] += 1

    sorted_index = 0
    for i in range(0, len(elements)):
        num = elements[i]
        while num > 0:
            arr[sorted_index] = i
            sorted_index += 1
            num -= 1

    return arr
