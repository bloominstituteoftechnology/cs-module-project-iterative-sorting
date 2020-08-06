# TO-DO: Complete the selection_sort() function below



 

def selection_sort(arr):
    for start in range(len(arr)):
        min = start
        
        for i in range(start, len(arr)):
            if arr[i]< arr[min]:
                min = i
                
        arr[start], arr[min] = arr[min] , arr[start]     
    return arr


            
# nums = [8,22,33,44,99,1]

nums2 = [108,64,68,23,33]
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0,len(arr)-1):
        
         for x in range(0,len(arr)-i-1):
             if arr[x]>arr[x+1]:
                 arr[x], arr[x+1]= arr[x+1], arr[x]
        
        

    return arr


print(bubble_sort(nums2))
# print(selection_sort(nums))
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

def insert_sort(nums):
    #loop through nums
    #list element is a sorted list of 1
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        
        while j>0 and temp < nums[j-1]:
            nums[j] = nums[j-1]
            j-=1
        nums[j] = temp   
    return nums    
    #inserting other elements into sorted sublist
    # shile n > LHS OR CURRENT INDEX IS  NOT 0
    #Swap
nums = [88,22,44,33]    
 
insert_sort(nums)
print("NEW",nums)