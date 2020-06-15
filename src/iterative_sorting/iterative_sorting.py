# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)-1): # for each element in the array, starting at the first index and finishing at the last index
        smallest_index = i # declare that the smallest index is the current index's value ("grab the first element so we can compare later")
        # TO-DO: find next smallest element
        for j in range(i+1, len(arr)): # loop through the remainder of the array, starting with the NEXT element and finishing with the last element
            if arr[j] < arr[smallest_index]: # if the element is less than the smallest index element 
                smallest_index = j # then make the smallest element that element
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] # 1, 0 = 0, 1
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


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