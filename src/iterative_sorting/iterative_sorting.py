import time

arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
arr2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    # (hint, can do in 3 loc)

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = arr[i]
        # TO-DO: find next smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < smallest_index:
                # update minimum if current is lower that we had previously
                smallest_index = arr[j]
                cur_index = j
        # Your code here

        # TO-DO: swap
        if cur_index is not i:
            arr[cur_index], arr[i] = arr[i], arr[cur_index]
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(1, len(arr)):
        # in every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
        for j in range(len(arr)-1):
            curr = arr[j]
            right = arr[j+1]
            if curr > right:
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


def counting_sort(arr, maximum=None):
    # Your code here

    return arr


start = time.time()
print("bubble sort", bubble_sort(arr))
end = time.time()
print(f"Runtime: {end-start}")


start = time.time()
print("selection sort", selection_sort(arr2))
end = time.time()
print(f"Runtime: {end-start}")
