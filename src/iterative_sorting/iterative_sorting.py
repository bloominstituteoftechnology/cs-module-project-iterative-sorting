# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): 
        min_value = i 
        for element in range(i+1, len(arr)):
            if arr[element] < arr[min_value]:
                min_value = element

        if min_value != i:
            arr[min_value], arr[i] =  arr[i], arr[min_value]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    indexing_length = len(arr) - 1

    # local variable
    sorted = False

    # as long as the sorted is false we will do the below actions
    while not sorted:
        sorted = True
        for i in range(0, indexing_length): # comparison
               # value to the left -> arr[i] # value to the right arr[i+1]
            if arr[i] > arr[i+1]:
                sorted = False
                # flip the two values
                arr[i], arr[i+1] = arr[i+1], arr[i]


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
