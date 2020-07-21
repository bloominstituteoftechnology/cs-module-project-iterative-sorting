def insertion_sort(array):
    """
    Sort the input array using the insertion sort algorithm.
    """
    # For every unsorted item:
    for i in range(1, len(array)):
        value = array[i]
        # Look "left" through sorted values until we find the right place to insert value:
        j = i
        while j > 0 and value < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        
        # Insert the value at that place:
        array[j] = value

    return array


def selection_sort(array):
    # Search all unsorted elements and find the lowest value:
    for i in range(0, len(array) - 1):
        current_index = i

        # Find next smallest element:
        smallest_index = current_index
        for j in range(current_index + 1, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
        
        # Swap the current value with the lowest value:
        array[current_index], array[smallest_index] = array[smallest_index], array[current_index]
    # Return sorted array:
    return array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


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
