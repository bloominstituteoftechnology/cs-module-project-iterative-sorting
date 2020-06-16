def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        next_value = arr[i]
        swap_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < next_value:
                next_value = arr[j]
                swap_index = j
        (arr[i], arr[swap_index]) = (next_value, arr[i])
    return arr


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        did_swap = False
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
                did_swap = True
        if not did_swap:
            return arr
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
    if len(arr) == 0:
        return []
    maximum = maximum if maximum is not None else max(arr)

    counts = [0] * (maximum + 1)

    for e in arr:
        if e < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[e] += 1

    output = []
    for element, count in enumerate(counts):
        if count > 0:
            for _ in range(0, count):
                output.append(element)
    return output
# time complexity: O(n+c) where c is the maximum
# space complexity: O(n+c)


test_count_sort = [4,4,9,4,1,0,3423,8,6,5,34,4,2,98,4,2,1,8,6]
sorted_arr = count_sort(test_count_sort)
print(sorted_arr)
