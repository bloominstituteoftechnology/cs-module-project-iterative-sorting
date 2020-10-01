# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index +1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                    
        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    #compare first and second item of arr
    count = 0
    while count < (len(arr)-1):
        # print(f'current array is now {arr}')
        if arr[count] > arr[count+1]:
            # print(f'{arr[count]} is bigger than {arr[count+1]} - swaping')
            #if the first item is bigger than the second, swap items
            arr[count], arr[count+1] = arr[count+1], arr[count]
            count = 0
        else:
            count +=1
        #repeat until end of list

    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

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
 - Stable
 - Time: O(n+k) where n is num itmes in array and k is range of values
 - Auxiliary Space: O(n+k) as creating new arrays
'''
def counting_sort(arr, maximum=None):
    # Your code here

    #find max

    #create buckets
    buckets = [0] * (maximum + 1)
    
    #Count each and every element in the array and increment its 
    # value at the corresponding index in the auxiliary array created
    for item in arr:
        buckets[item] +=1
    
    #Find cumulative sum is the auxiliary array we adding curr and prev frequency
    pass

    #Now the cumulative value actually signifies the actual location of the element in the sorted input array
    pass

    #Start iterating auxiliary array from 0 to max
    pass

    #Put 0 at the corresponding index and reduce the count by 1, which will signify the second position 
    # of the element if it exists in the input array
    pass

    # Now transfer array received in the above step in the actual input array
    pass

    return arr


counting_sort([1,2,3], 3)