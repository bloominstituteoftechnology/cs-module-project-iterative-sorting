# Consider the first element to be sorted and the rest to be unsorted
# Assume the first element to be the smallest element.
# Check if the first element is smaller than each of the other elements:
# If yes, do nothing
# If no, choose the other smaller element as minimum and repeat step 3
# After completion of one iteration through the list, swap the smallest element with the first element of the list.
# Now consider the second element in the list to be the smallest and so on till all the elements in the list are covered.
# Once an element is added to the sorted portion of the list, it must never be touched and or compared.
# https://www.pythoncentral.io/selection-sort-implementation-guide/ 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) -1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range (cur_index+1,len(arr)):
            if arr[smallest_index]>arr[j]:
                smallest_index = j

        # TO-DO: swap
        arr[i],arr[smallest_index] = arr[smallest_index],arr[i]
        #print (arr)
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
# For the first iteration, compare all the elements (n). For the subsequent runs, compare (n-1) (n-2) and so on.
# Compare each element with its right side neighbour.
# Swap the smallest element to the left.
# Keep repeating steps 1-3 until the whole list is covered.
# https://www.pythoncentral.io/bubble-sort-implementation-guide/ 
    for j in range(len(arr)-1,0,-1):
        for i in range (j):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp 
        #print (arr)

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
