# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    
    changed = False
    prev = 0
    for cur in range(len(arr)):
        if arr[cur] < arr[prev]:
            temp = arr[prev]
            arr[prev] = arr[cur]
            arr[cur] = temp
            changed = True
        
        prev = cur

    if changed:
        return bubble_sort(arr)
    else:
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
    # maximum + 1 is needed because we are using values as indexes.  But since
    # arrays start at index 0, our maximum value is actually one past the array
    # length.

    # maximum is not actually used in the test cases
    # buckets = [0] * (maximum + 1)
    buckets = []

    for ele in arr:
        if ele < 0:
            return 'Error, negative numbers not allowed in Count Sort'

        # This section grows my buckets array as we iterate, since no max was
        # given.
        if (ele + 1) > len(buckets):
            grow_by = (ele + 1) - len(buckets)
            extension = [0] * grow_by
            extension[-1] = 1
            buckets.extend(extension)
        else:
            buckets[ele] += 1

    counter = 0
    for i in range(len(buckets)):
        how_many = buckets[i]

        while how_many > 0:
            arr[counter] = i
            counter += 1
            how_many -= 1

    return arr
