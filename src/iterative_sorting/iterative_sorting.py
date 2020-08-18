# python3 src/iterative_sorting/test_iterative.py -v


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # Loop through the elements
    for i in range(len(arr)):
        current = i
        smallest = current
        # Find next smallest element
        for j in range(i+1, len(arr)): 
            if arr[smallest] > arr[j]: 
                smallest = j 
         # Swap elements
        arr[i], arr[smallest] = arr[smallest], arr[i] 

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements 
    for i in range(n-1):
        # Last i elements are already in place 
        for j in range(n-1):
            # Swap if the element found is greater than the next element 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
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
import numpy as np

def counting_sort(arr, maximum=None):
    if len(arr) == 0:
        return arr
    
    count_negatives = 0
    for i in arr:
        if i < 0:
            count_negatives += 1

    if count_negatives > 0:
        return "Error, negative numbers not allowed in Count Sort"

    else:
        buckets = [0] * (np.max(arr) + 1)
        for i in range(0, (len(buckets))):
            for j in arr:
                if i == j:
                    buckets[i] += 1

        for i in range(len(arr)):
            if i < 1:
                for j in range(len(buckets)):
                    n = buckets[j]
                    if i < len(arr):
                        if buckets[j] != 0:
                            for k in range(i, i + n):
                                arr[k] = j
                        i = i + n 
    
    return arr
