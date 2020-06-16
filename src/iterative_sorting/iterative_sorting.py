def selection_sort(arr):
    """
    Selection Sort algorithm implementation
    
    Args:
        arr: Array of values to sort

    Returns:
        arr: Sorted array

    Examples:
        >>> arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        >>> sorted_arr1 = selection_sort(arr1)
        >>> print(sorted_arr1)
        [0,1,2,3,4,5,6,7,8,9]
    """

    # For all indices EXCEPT the last index
    for i in range(0, len(arr) - 1):
        # Start with current index = 0
        cur_index = i
        smallest_index = cur_index
        #a. Loop through elements on right-hand-side 
        # of current index and find the smallest element
        for j in range(i+1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j
        # b. Swap the element at current index with the 
        # smallest element found in above loop
        arr[i], arr[cur_index] = arr[cur_index], arr[i]
    return arr


def bubble_sort(arr):
    """
    Bubble Sort algorithm implementation
    
    Args:
        arr: Array of values to sort

    Returns:
        arr: Sorted array

    Examples:
        >>> arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        >>> sorted_arr1 = bubble_sort(arr1)
        >>> print(sorted_arr1)
        [0,1,2,3,4,5,6,7,8,9]
    """

    # Loop through your array
    for i in range(len(arr)-1):
        swapped = False
        # Compare each element to its neighbor
        for j in range(0, len(arr)-i-1):
            # If elements in wrong position 
            # (relative to each other, swap them)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps performed, stop. 
        # Else, go back to the element at index 0 
        # and repeat step 1.
        if swapped == False:
            break
    return arr


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
def count_sort(arr, maximum=None):

    return arr
