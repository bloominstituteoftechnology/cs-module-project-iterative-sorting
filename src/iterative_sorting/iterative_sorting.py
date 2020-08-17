# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
#     length = len(arr)
#    #Traverse through the array
#     for index in range(length - 1):
#        #Travers through the arr[index] - 1
#         lower_index = length - index - 1
#         for index2 in range(0, arr[lower_index]):
#             index2_next_index = index2 + 1
#            # Swap if the element found is greater
#             if arr[index2] > arr[(index2_next_index)]:
#                 arr[index2], arr[index2_next_index] = arr[index2_next_index], arr[index2]
    length = len(arr)

    for index in range(length):
        swapped: bool = False

        smaller_range = length - index - 1
        for index2 in range(0, smaller_range):
            next_index = index2 + 1
            if arr[index2] > arr[next_index]:
                arr[index2], arr[next_index] = arr[next_index], arr[index2]
                swapped = True
        if swapped == False:
            break
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
