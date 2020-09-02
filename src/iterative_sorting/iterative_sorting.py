def selection_sort(arr):
    # Outer loop for all elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Inner loop to check for next smallest index - compare next element to current one and, if smaller, set smallest element to j
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Swap smallest element with current element
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

def bubble_sort(arr):
    # Loop through all elements
    for i in range(len(arr)):
        # Moving largest element far right sets it in place so inner loop can be one less than current index each pass
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if next element is smaller than current one
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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
# def counting_sort(arr, maximum=None):
#     # Your code here

#     return arr
