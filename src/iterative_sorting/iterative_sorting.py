# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # for each value in the range of values between the smallest index and the length of the array
        for j in range(smallest_index, len(arr)):
            # if the value of the smallest index is greater than the value of the element being compared
            if arr[smallest_index] > arr[j]:
                # make this new index the smallest index
                smallest_index = j
            # once this has checked every value, we can move onto the next step of swapping
        # TO-DO: swap
        # Your code here
        # take the index position of the array , and the index position for the smallest value, and swap them
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # assign a var to the length of the array
    n = len(arr)
    # traverse through all array elements
    for i in range(n-1):
    # range(n) also works but outer loop will repeat one more time than needed

        # last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # swap if the element found is greater than the next element

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # This will only make swaps in pairs as opposed to swapping any two locational values

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
    arr = [0 for i in range(maximum)]
    

    return arr

