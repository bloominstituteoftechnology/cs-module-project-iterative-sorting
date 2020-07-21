# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements

    # run an outerloop
    for i in range(len(arr)):

        # set current index to i
        cur_index = i

        # run an inner loop from i + 1 which mean value next to i on the right
        for j in range(i + 1, len(arr)):

            # if next value less than current value
            if arr[j] < arr[cur_index]:
                # then we set current index to j
                cur_index = j

        if cur_index != i:
            # if current index different than i
            # swap the value and continue the loop until the inner if statement is false
            arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    # get last index of the list
    indexing_length = len(arr) - 1

    # create a variable called sorted
    sorted = False

    while sorted is False:

        sorted = True

        for i in range(0, indexing_length):

            # compare current value to the next value
            if arr[i] > arr[i + 1]:

                # if current value > next value we will swap them and set sorted = False

                # if current value < next value we don't swap or set sorted, hence sorted remain True

                # and we break out of the loop
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                sorted = False


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


selection_sort([7, 2, 5, 10, 3])
