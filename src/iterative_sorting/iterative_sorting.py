# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for x in range(i + 1, len(arr)):
            if arr[x] < arr[smallest_index]: # check if smaller than current smallest
                smallest_index = x # set to smallest

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# printThis = selection_sort([12,5,10,13,1,7,93,15])
# print(printThis)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for t in range(len(arr)):
        for e in range(0, len(arr)-t-1):
            if arr[e]> arr[e+1]:
                arr[e], arr[e+1] = arr[e+1], arr[e]

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
