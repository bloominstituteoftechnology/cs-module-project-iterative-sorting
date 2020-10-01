# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print(f'we are investigating arr: {arr}')
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(f'Again for i: {i}, now the smallest index is: {smallest_index}')
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        print('i: ', i)
        for j in range(cur_index+1, len(arr)):
            print('j: ', j)
            if arr[j] < arr[smallest_index]:
                print(f'{arr[j]} is less than {arr[smallest_index]}!')
                smallest_index = j
                print(f'now the smallest element is: {arr[smallest_index]}')
                print(f'now the smallest index is: {smallest_index}')

        # TO-DO: swap
        # Your code here
        print(f'we are swapping {arr[smallest_index]} and {arr[cur_index]}')
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        
        print(f'for i: {i} we have arr: {arr}\n')

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


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
