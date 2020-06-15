# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        print(f"Selection Sort Array {arr}")
        # loop through range of remaining unsorted 
        for j in range(current_index + 1, len(arr)):
            
            # check if value of unsorted portion is smaller than the current smallest
            if arr[j] < arr[smallest_index]:

                # if it set new smallest index
                smallest_index = j
        # TO-DO: swap
        # Your code here
        # temporary holder for value of item at input array's current index
        temp = arr[current_index]

        # overwrite value at input array's current index with smallest index value
        arr[current_index] = arr[smallest_index]

        # set item at input array's old smallest index spot to the temp placeholder above
        arr[smallest_index] = temp
        
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr)): 
        # amount of already sorted indices, the + 1 is because we are subtracting sorted_indices from the len to offset 0 index
        sorted_indices = i + 1
        # iterate from 0 index to last unsorted index
        for j in range(0, len(arr) - sorted_indices):
            # if next index is less than 
            # check if 
            if arr[j] > arr[j + 1]:
            # if j + 1 < len(arr) and arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

    return arr

some_list = [2, 6, 5, 10, 8, 4, 7, 9, 3, 1]
x = selection_sort(some_list)
print(f"Selection Sort 1: {x}")
some_list = [2, 6, 5, 10, 8, 4, 7, 9, 3, 1]
x = bubble_sort(some_list)
print(f"Bubble Sort 1: {x}")
some_list2 = [9, 10, 3, 4, 5, 6, 7, 8, 1, 2]
x = selection_sort(some_list2)
print(f"Selection Sort 2: {x}")
some_list2 = [9, 10, 3, 4, 5, 6, 7, 8, 1, 2]
x = bubble_sort(some_list2)
print(f"Bubble Sort 2: {x}")
some_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
x = selection_sort(some_list3)
print(f"Selection Sort 3: {x}")
some_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
x = bubble_sort(some_list3)
print(f"Bubble Sort 3: {x}")
some_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]
x = bubble_sort(some_list4)
print(f"Bubble Sort 4: {x}")
'''
STRETCH: implement the Count Sort function below

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
