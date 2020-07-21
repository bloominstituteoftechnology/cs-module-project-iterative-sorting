def selection_sort(arr):
    #Move through the entire array
    for i in range(len(arr)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
              
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr): 
    n = len(arr) 
   
    # Move through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
    
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
# def counting_sort(arr, maximum=None):
#     # Your code here


#     return arr
