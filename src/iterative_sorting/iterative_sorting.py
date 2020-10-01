# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through arr
    Swapped = False
    while not Swapped:
        Swapped = True
        for i in range(0, len(arr) - 1):
            # compare each element to its neighbor
            # if element in wrong position, swap them
            # Once sorted, the for loop won't use this if statement again so the Swapped
            # remains True breaking us out of the loop
            if arr[i] > arr[i + 1]:
                Swapped = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


    # if no swaps performed, stop
    # else, go back to the element at index 0 and repeat step 1.

list_to_sort = [7,22,33,11,44]

x = bubble_sort(list_to_sort)
print(x)
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
