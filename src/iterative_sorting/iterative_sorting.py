"""
Iterative sorting module.
"""
import numpy as np

def selection_sort(arr):
    """
    Selection sort repeatedly finds and selects the next smallest element,
    then inserts it in its designated place.
    """

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # Find next smallest element.
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Swap.
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = \
                arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort(arr):
    """
    In Bubble Sort, we make a series of swaps between adjacent elements,
    gradually moving larger elements towards the end of the array (or bubbling
    larger elements up).
    """

    num_swaps = 1
    while num_swaps != 0:
        num_swaps = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                num_swaps += 1

    return arr


def counting_sort(arr, maximum=None):
    """
    STRETCH: Implement the Count Sort function.

    Counting sort is a sorting algorithm that works on a set of data where
    we specifically know the maximum value that can exist in that set of
    data. The idea behind this algorithm then is that we can create "buckets"
    from 0 up to the max value. This is most easily done by initializing an
    array of 0s whose length is the max value + 1 (to accommodate zero values).

    Each buckets[i] then is responsible for keeping track of how many times
    we've seen `i` in the input set of data as we iterate through it.
    Once we know exactly how many times each piece of data in the input set
    showed up, we can construct a sorted set of the input data from the
    buckets.

    The counting sort algorithm has time and space complexity O(n), where n is
    the greater of the array length or the maximum value. If the minimum value
    is also known, then it's O(n), where n is the greater of the array length
    or the difference between the minimum and maximum values.
    """

    # Find the maximum value:
    if maximum is None:
        try:
            maximum = max(arr)
        except ValueError:
            return []

    # Store the count of each unique object.
    count = np.zeros(maximum + 1)
    for num in arr:
        if num < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        count[num] += 1

    # Make the count array cumulative.
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output_arr = arr.copy()
    for num in arr:
        output_arr[int(count[num]) - 1] = num
        count[num] -= 1

    return output_arr
