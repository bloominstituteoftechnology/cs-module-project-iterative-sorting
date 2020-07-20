# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # for each element in current index+1 to length of array
        for j in range(cur_index, len(arr)):
            # if item is < smallest index, capture smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        # update smallest and current
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    # Your code here

    # Run through array
    for i in range(len(arr)):
        # go through items
        for j in range(len(arr)-1-i):
            # compare if greater
            if arr[j] > arr[j+1]:
                # swap
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


def counting_sort(arr, maximum=-1):
    # Your code here
    counter = []
    for i in range(len(arr)):
        if arr[i] < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        if arr[i] > maximum:
            maximum = arr[i]
            counter += [0] * ((maximum + 1) - len(counter))
        counter[arr[i]] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]
    counter.insert(0, 0)
    counter.pop()
    new = [0] * len(arr)
    for x in arr:
        new[counter[x]] = x
        counter[x] -= 1
    return new
