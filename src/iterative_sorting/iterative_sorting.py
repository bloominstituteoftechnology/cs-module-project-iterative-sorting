# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    length = len(arr)
    for i in range(0, length):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if i != smallest_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                

    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        for j in range(i+1, len(arr)):
            if value < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = value
            else:
                break
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
    if maximum is None:
        if len(arr) > 0:
            maximum = max(arr)
        else:
            return arr
    buckets = [0 for i in range(maximum + 1)]
    
    for val in arr:
        if val < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[val] += 1
    output = []
    for index, count in enumerate(buckets):
        if count > 0:
            output.extend([index for i in range(count)])
    return output
        
