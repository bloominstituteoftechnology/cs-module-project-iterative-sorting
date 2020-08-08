# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) ):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # For all indices EXCEPT the last index:
        for smallest_index in range(i+1, len(arr)):
            # a. Loop through elements on right-hand-side of current index and find the smallest element
           if arr[smallest_index] < arr[cur_index]:
               cur_index = smallest_index
        # b. Swap the element at current index with the smallest element found in above loop
        arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Loop through your array
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
        # Compare each element to its neighbor
            # print(arr[j], arr[curr_index])
            if arr[j] > arr[j + 1]:
    #     If elements in wrong position (relative to each other, swap them)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(arr[i], arr[j], arr[curr_index])
                # break
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.


    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr2 = []
# arr3 = [0, 1, 2, 3, 4, 5]

print(selection_sort(arr1))
# print(bubble_sort(arr1))

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
