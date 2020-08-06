# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): #* for i in range of 0, length of arr minus 1
        cur_index = i #* cur index is equal to i
        smallest_index = cur_index #* smallest index is equal to cur index
        # TO-DO: find next smallest element
        for x in range(cur_index + 1, len(arr)): #* for x in range of cur index plus 1 and length of arr
            if arr[x] < arr[smallest_index]: #* if x in arr is greater than smallest index in arr
                smallest_index = x #* smallest index is equal to x
        # (hint, can do in 3 loc)
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    x = len(arr) #* x is equal to the length of arr
    for i in range(x-1): #* for i in range of x minus 1
        for y in range(0, x-i-1): #* for y in range of 0, x minus i minus 1
            if arr[y] > arr[y+1]: #* if y in arr is greater than y in arr plus one
                arr[y], arr[y+1] = arr[y+1], arr[y] #* swap it



    return arr

#* ALL TESTS PASSED

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
