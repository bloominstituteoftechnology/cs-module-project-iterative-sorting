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
        swap = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = swap

    return arr

## FROM LECTURE
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         sorted_boundary = i
#         smallest_index = sorted_boundary
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         # Your code here
#         # iterate through the unsorted portion of the array
#         # finding the index of the smallest element in the unsorted portion
#         for unsorted_index in range(sorted_boundary, len(arr)):
#             # if we find a value < smallest_index element,
#             # update our smallest_index variable
#             if arr[unsorted_index] < arr[smallest_index]:
#                 smallest_index = unsorted_index

# # TO-DO: swap
# # Your code here
# # we've found the smallest element in the unsorted portion
# # swap it with the element right next to the boundary
# arr[smallest_index], arr[sorted_boundary] = arr[sorted_boundary], arr[smallest_index]
# ​
# return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = swap
                swap += 1

    return arr

## FROM LECTURE - Iterative bubble sort implementation:
# def bubble_sort(arr):
# 	# it traverses the array
#     # loop until no more swaps occur
#     swaps_occurred = True

# ​
#    while swaps_occurred:
#         swaps_occurred = False
# ​
#        for i in range(0, len(arr)-1):
#             # compare two elements
#             if arr[i] > arr[i+1]:
#                 # swaps them if the two elements aren't in order
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swaps_occurred = True

# 	return arr


## FROM LECTURE - Recursive bubble sort implementation:
# def bubble_sort(arr, unsorted_length):
#     # find the unsorted_length
#     # iterate through the arr
#     # figure out, starting from the right side, how many elements
#     # of the array are sorted
#     # recursive implementation of bubble sort
#     # base case
#     # what's the length of the unsorted portion of our array?
#     # once we get to an empty unsorted portion, then everything is sorted
#     # how are we moving closer to our base case?
#     for i in range(0, unsorted_length - 1):
#         # compare two elements
#         if arr[i] > arr[i+1]:
#             # swaps them if the two elements aren't in order
#             arr[i], arr[i+1] = arr[i+1], arr[i]


# ​
# # we've done one iteration of the swapping, check to see
# # if there's more sorting to do
# if unsorted_length > 0:
#     bubble_sort(arr, unsorted_length - 1)


"""
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
"""


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
