# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    #print(arr)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        j = i
        #print(f'i:{i}')
        #print(f'len array {len(arr)}')
        while j < (len(arr)):
            #print(cur_index+j)
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                #print(f'next smallest number: {arr[smallest_index]}')
            #print(f'current j{j}')
            j += 1
            #print(f'new j{j}')

        # TO-DO: swap
        # Your code here
        #swap the smallest card with whatever is at index 0
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
        #print(arr)




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    #print(arr)
    #print("--------")


    ## compare first index with neighbor to right
    ## if the neigbor on the right is less than the left, swap them
    for number in range(0, len(arr)-1):
        i = 0
        while i < (len(arr)-1):     
            if arr[i+1] < arr[i]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            i+=1
            #print(i)
    
    ## otherwise do nothing
    
    #print(arr)
    #after this pass, the farthest right value should be the largest

    #if at least one swap was done:
    #repeat this process


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
