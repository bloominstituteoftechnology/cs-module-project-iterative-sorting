# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # will loop through the rest of the array and if I 
        # find one smaller I will make the smallest index point at 
        # the index that is the smallest
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                # reassinging the smallest index
                smallest_index = j
        # doing the swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    hasSwaped = True
    while hasSwaped:
        # setting hasSwaped to false if there was no swap
        hasSwaped = False
        # looping through the array
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                # putting that there was a swap
                hasSwaped = True


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
    # checking to see if there is a empty list
    if not arr:
        return arr
    # checking to see if the maximum == none
    if not maximum:
        maximum  = arr[0]
        for i in range(len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
    # creating the array of the buckets
    bucket_arry = [0] * (maximum + 1)
   
    # Looping through the array an counting the number of times
    # that the i is seen in the arr
    for i in range(len(arr)):
        # adding up the occurences of the elements
        if arr[i] >= 0: # making sure that it is not negative numbers
            bucket_arry[arr[i]] += 1
        else:
            # going to stop and return a string that 
            # says that can't have negative numbers
            return "Error, negative numbers not allowed in Count Sort"
    # now will be looping through and then adding
    # up to find the index where the items starts
    
    for i in range(len(bucket_arry)-1):
        
        bucket_arry[i + 1] = bucket_arry[i] + bucket_arry[i+1]
    # now filling the arr with the values
    # doing the first line before doing a loop
    arr[:bucket_arry[1]] = [0] * bucket_arry[1]
    for i in range(len(bucket_arry)-1):
        arr[bucket_arry[i]:bucket_arry[i+1]] = [i+1] * abs(bucket_arry[i] - bucket_arry[i+1])

    return arr
