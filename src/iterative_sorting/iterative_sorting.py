# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for x in range(smallest_index, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for x in range(0, len(arr) - i - 1):
            current = x
            right = x + 1
            if arr[current] > arr[right]:
                arr[current], arr[right] = arr[right], arr[current]

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
    if not arr:
        return arr

    if any(x < 0 for x in arr):
        return "Error, negative numbers not allowed in Count Sort"

    if maximum:
        buckets = [0] * (arr + 1)

    else:
        buckets = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        buckets[i] += 1
        buckets[i] += buckets[i-1]
        arr[i] = buckets[i] - 1

    return arr

