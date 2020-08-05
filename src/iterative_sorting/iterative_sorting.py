# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for cur_index in range(0, len(arr) - 1):
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for n in range(len(arr), 1, -1):
        for i, elem in enumerate(arr[1:n]):
            if elem < arr[i]:
                arr[i], arr[i+1] = elem, arr[i]
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
# Time Complexity: O(n + maximum), which simplifies to O(n)
# Space Complexity: O(n + maximum), which simplifies to O(n)
def counting_sort(arr, maximum=None):
    if len(arr) < 2:
        return arr
    
    if maximum is None:
        # Time Complexity: O(n)
        maximum = max(arr)
    
    # Time Complexity: O(maximum)
    # Space Complexity: O(maximum)
    buckets = [0] * (maximum + 1)

    # Time Complexity: O(n)
    for elem in arr:
        if elem < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[elem] += 1
    
    i = 0
    # Time Complexity: O(n + maximum)
    for bucket_index in range(maximum + 1):
        for _ in range(buckets[bucket_index]):
            arr[i] = bucket_index
            i += 1

    return arr
