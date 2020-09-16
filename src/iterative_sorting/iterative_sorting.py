# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print("Starting sort.")
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for n in range(i, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n
        # TO-DO: swap
        # Your code here
        smallest = arr[smallest_index]
        del arr[smallest_index]
        arr.insert(i, smallest)
        print(f"Moved {smallest} to index: {smallest_index}")

    print("Finished sorting list.")
    print(f"{arr}")
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    finished = False
    sorts_count = 0
    arr_range_max = len(arr) - 1
     
    print("Starting sort.")
    while finished is not True:
        for i in range(0, arr_range_max):
            left_index = i
            right_index = i + 1
            lhs = arr[left_index]
            rhs = arr[right_index]

            print(f"left: {lhs} right: {rhs}")

            if lhs > rhs:
                del arr[right_index]
                arr.insert(left_index, rhs)
                sorts_count += 1

            if right_index == arr_range_max:
                if sorts_count == 0:
                    print(f"Finished sorting list.")
                    finished = True
                else:
                    print(f"Sorted {sorts_count} times. Re-starting.")
                    sorts_count = 0
                    continue
    print(f"{arr}")
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
        return arr
    if maximum is None:
        maximum = max(arr)

    buckets = [0 for i in range(maximum + 1)]

    for value in arr:
        if value < 0:
            return "Error negative numbers not allowed for count sort."
        buckets[value] += 1

    output = []

    for index, count in enumerate(buckets):
        output.extend([index for i in range(count)])

    return output

#my_arr = [23, 8, 42, 4, 16, 15]
#bubble_sort(my_arr)
#selection_sort(my_arr)