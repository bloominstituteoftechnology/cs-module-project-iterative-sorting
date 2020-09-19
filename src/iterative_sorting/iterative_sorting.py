# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(cur_index + 1, len(arr)):
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    end_of_list = len(arr)
    current_index = 0

    # Compare the first and second item of a collection. If the first item is bigger than the second item, swap the items.
    for _ in range(len(arr)):
    # Move to the next item. Now, we will compare the second item with the third item. If the second item is bigger than the third, swap the items.   
        for compare in range(current_index + 1,end_of_list):
            # print(f"C {compare} CI {current_index}")
            # print(f"{arr[current_index]} {arr[compare]}")

            if arr[current_index] > arr[compare]:
                arr[current_index], arr[compare] = arr[compare], arr[current_index]
                current_index += 1

            else: 
                current_index += 1
            

        end_of_list -= 1
        current_index = 0

    # Do this for every item until the end of the list.
    # Repeat steps 1-3 (decrementing “the end of the list” by 1 each time).


    print(arr)

    return arr

arrayboii = [12,21,8,14,29, 40, 30, 20, 88]
bubble_sort(arrayboii)

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
