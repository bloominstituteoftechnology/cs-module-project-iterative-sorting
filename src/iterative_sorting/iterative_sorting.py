# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)- 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        j = i
        lowest = 1000000
        lowest_index = j
        while j <= len(arr) - 1:
            if arr[j] < lowest:
                lowest = arr[j]
                lowest_index = j
            j += 1



        # TO-DO: swap
        arr[lowest_index], arr[cur_index] = arr[cur_index], lowest
        # Your code here

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    moved = True
    while moved:
        moved = False
        for i in range(0, len(arr) - 1):
            right = i + 1
            left = i
            if arr[left] > arr[right]:
                arr[right], arr[left] = arr[left], arr[right]
                moved = True
            
    



    return arr

print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))

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
    count = []
    final = []
    for i in range(1, maximum):
        count.append(arr.count(i))
    def multi_append(arr, val, times):
        while times > 0:
            arr.append(val)
            time -= 1
    for j in count:
        multi_append(final, j + 1, count[j])




    return arr

