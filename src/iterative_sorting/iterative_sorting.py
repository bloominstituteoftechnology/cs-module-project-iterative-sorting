# TO-DO: Complete the selection_sort() function below
def swap(array, firstIndex, secondIndex):
  temp = array[firstIndex]
  array[firstIndex] = array[secondIndex]
  array[secondIndex] = temp

  

def selection_sort(array):
  # Write this method
  for i in range(len(array) - 1):
    #set the first item in array as mininum value by default
    min = i
    #check the element to be next minimum value
    for j in range(i+1, len(array)):
      if array[j] < array[min]:
        min = j
    
    swap(array, min, i)

  return



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
        for i in range(0,len(arr)-1):
            for j in range(0, len(arr) -1 -i):
                if arr[j] > arr[j + 1]:
                   arr[j], arr[j+1] = arr[j+1], arr[j] 
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
