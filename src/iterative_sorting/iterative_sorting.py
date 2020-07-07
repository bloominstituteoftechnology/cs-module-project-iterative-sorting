# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # loops through all values and compares to find smallest.
        # then will go to next i in array
        for j in range(cur_index, len(arr)):
            #find lowest value
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr
arrS = [4,5,1,55,3,4,0,1]
print('selection', selection_sort(arrS))
       
# starts at 0 index in array, compares to all other numbers in the array.  
# finds the smallest number and then swaps with the smallest number.
# so now the smallest number is in index 0, next will take index 1 and compare to all numbers greater than index 1
#finds the smallest number and puts at index 1 by making a swap.


# arr1 = [1, 5, 8]
# for x in range(len(arr1)):
#     print(x)

# result1 = selection_sort(arr1)
# print(result1)

# TO-DO:  implement the Bubble Sort function below
#bubble only compares direct neighbors
def bubble_sort(arr):
    # Your code here
# loop through n-1 elements
    for i in range(0, len(arr)):
    #     cur_index = i
    #    # print('cur_index', cur_index)
    #     smallest_index = cur_index
    #    # print('smallest_index', smallest_index)
    #     # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc)
    #     # Your code here
    #     print('arr i', arr[i], 'smallest_index', smallest_index)
    #     if arr[i] < smallest_index:
    #         smallest_index = arr[i]

        # TO-DO: swap
        # Your code here
        # this way we will not compare the first element to the first element
        # and have a way to end the while loop 
        while i - 1 >= 0:
            #value of temp 
            #sets temp to previous value
            temp = arr[i - 1]
            if arr[i] < temp:
                #previous = current value
                arr[i - 1] = arr[i]
                #make temp current value
                arr[i] = temp
                i -= 1
            else:
                # if temp, (previous value), is less.  will end while loop and, and iterate next value on for loop
                # to end the while loop
                break

    return arr
arr1 = [1, 5, 8, 4, 29, 9, 6, 0, 3, 7, 9, 67]
result2 = bubble_sort(arr1)
print(result2)


'''
STRETCH: implement the Count Sort function below

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
#required to know max value wil be sorting

def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr

    if maximum == None:
        #set maximum to max value in array
        maximum = max(arr)

    #make a bunch of buckets 
    # make a bucket to hold each possible value
    #will create 0s, _ means not using i
    #takes max number + 1 and creates buckets for each number.
    #maximum = 19, will create 20 buckets
    # maximum + 1, because first bucket will be 0
    buckets = [0 for _ in range(maximum+1)]
    

    # buckets are now in an array of 0s,
    # if the number is in the array it will add a 1 to that index in the array
    # example if [2,2,2,20]  will be 21 buckets , and bucket[2] = 3
    for x in arr:
        if x < 0:
            return 'Error, negative numbers not allowed'
        buckets [x] += 1
    
    #we have a count for each bucket
    #Ex. use case, how many sessions on this date
    # will write array values out in order, will be sorted
    j = 0
    for i in range(len(buckets)):
        #while value of the bucket is > o
        #print that index, index is already equal to value
        # only looks for buckets > 0
        while buckets[i] > 0:
            arr[j] = i
            # j tracks index of array
            j += 1
            buckets[i] -= 1
    print(arr)
    return arr


arr1 = [1, 1, 19, 2,5,4]
print(counting_sort(arr1))
