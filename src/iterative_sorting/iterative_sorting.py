# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i,len(arr)):
            smallest_index = j if (arr[j] < arr[smallest_index]) else smallest_index

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swapped = True


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
    
    if len(arr) == 0:
        return []

    if maximum is None:
        maximum = max(arr)

    if len([x for x in arr if x < 0]) > 0:
        return "Error, negative numbers not allowed in Count Sort"


    counts = [0] * (maximum + 1)
    for i in range(len(counts)):
        for j in range(len(arr)):
            if i == arr[j]:
                counts[i] += 1
    

    arr = []
    for k in range(len(counts)):
        if counts[k] > 0:
            arr.extend([k] * counts[k])


    return arr

if __name__ == "__main__":
    import random

    arr4 = random.sample(range(200), 50)
    print(arr4)
    print(" ")
    print(counting_sort(arr4))
