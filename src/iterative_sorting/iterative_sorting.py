def selection_sort(arr):
    for index in range(len(arr)):
        lowest = index #default to current index
        
        for index2 in range(index + 1, len(arr)): #check out everything after this index
            if arr[index2] < arr[lowest]: #anything lower?
                lowest = index2
                
        if index is not lowest:
            arr[index], arr[lowest] = arr[lowest], arr[index] #swap current with lowest
            
        return arr
        
def bubble_sort(arr):
    isFinished = False
    
    while isFinished is False:
        isFinished = True
        
        for index in range(1, len(arr)): #range starts at [1], compares against previous [0]
            if arr[index] < arr[index-1]:
                arr[index], arr[index-1] = arr[index-1], arr[index] #swap values
                isFinished = False
    
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
