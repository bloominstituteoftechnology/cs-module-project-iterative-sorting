# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    i = 1
    swapped = True
    while swapped:
        swapped = False
        for j in range(0, len(arr) - i):
            a = arr[j]
            b = arr[j + 1]
            if a > b:
                arr[j] = b
                arr[j + 1] = a
                swapped = True
        i += 1

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
    if len(arr) == 0:
        return []

    if maximum is None:
        maximum = get_max(arr)
        if maximum is None:
            return []

    counts = []
    for _ in range(maximum + 1):
        counts.append(0)

    for i in range(len(arr)):
        val = arr[i]
        if val < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[val] += 1

    sorted = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            sorted.append(i)
    return sorted


def get_max(arr):
    max = None
    for i in arr:
        if max is None:
            max = i
        elif i > max:
            max = i
    return max
