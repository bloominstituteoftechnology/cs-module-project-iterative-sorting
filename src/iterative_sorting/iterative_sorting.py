import time

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for index in range(i+1, len(arr)):
            if arr[smallest_index]>arr[index]:
                smallest_index=index

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index]=arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # def swap(i, j):
    #    arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
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
    start_time=time.time()
    if len(arr) < 2:
        return arr

    if maximum is None:
        # Time Comp: O(n)
        maximum = max(arr)

    # Time Comp: O(1)
    # Space Comp: O(1)
    container = [0] * (maximum + 1)

    # Time Comp: O(n)
    for element in arr:
        if element < 0:
            return "Error, negative numbers not allowed in Count Sort"
        container[element] += 1

    i = 0
    
    # Time Comp: O(1)
    for cont_index in range(maximum + 1):
        for index in range(container[cont_index]):
            arr[i] = cont_index
            i += 1
    end_time=time.time()
    print(f"runtime: {end_time - start_time} seconds")
    return arr


