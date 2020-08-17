# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
#     length = len(arr)
#    #Traverse through the array
#     for index in range(length - 1):
#        #Travers through the arr[index] - 1
#         lower_index = length - index - 1
#         for index2 in range(0, arr[lower_index]):
#             index2_next_index = index2 + 1
#            # Swap if the element found is greater
#             if arr[index2] > arr[(index2_next_index)]:
#                 arr[index2], arr[index2_next_index] = arr[index2_next_index], arr[index2]
    length = len(arr)

    for index in range(length):
        swapped: bool = False

        smaller_range = length - index - 1
        for index2 in range(0, smaller_range):
            next_index = index2 + 1
            if arr[index2] > arr[next_index]:
                arr[index2], arr[next_index] = arr[next_index], arr[index2]
                swapped = True
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
def counting_sort(arr, maximum=None):

    '''
    Input:
index    1  2  3  4  5  6  7
        [1, 2, 3, 3, 3, 2, 1], maximum: 3
    Output:
        [1, 1, 2, 2, 2, 3, 3]

    1.  Store the length of the array.  
        Create a storage container for the sorted array.

    2. Create an array of zeros which is one element longer that the maximum value,
        in which to save the count of occurences of each value

index    1  2  3  4  5  6  7
        [1, 2, 3, 3, 3, 2, 1]

index        0  1  2  3
represents   0  1  2  3
            [0, 0, 0, 0] - counts array

    3. Loop through the input array.
    
    4.  Increment the element count for the value from the input array in the counts array
        4.1 - Get the value of the index from the original array
        4.2 - Increment the value at the index of value 4.1 in the counts array

index    1  2  3  4  5  6  7
        [1, 2, 3, 3, 3, 2, 1]

index        0  1  2  3
represents   0  1  2  3
            [0, 2, 3, 2]

    5. Loop through the count array.
    
    6. Store the cumulative sum of the elements of the count array. 
    (Add the current element's value plus the previous element's value, and set to the current element's value)

index        0  1  2  3
represents   0  1  2  3
            [0, 2, 3, 2]

            0 + 2 = 2
            2 + 3 = 5
            5 + 2 = 7

                 |
                 |
                 v

index        0  1  2  3
represents   0  1  2  3
            [0, 2, 5, 7]

    7. Find the index of each element of the original array in the count array. 
        Assign to Output array.

        7.1 - Get the value at every index in the original array

        7.2 - Get the value at the the 7.1 indext in the counts array

        7.3 - Decrement 7.2 by 1

        7.4 - Assign the index of the counts array as the value for the index at 7.3 in the output array 

         1  2  3  4  5  6  7
        [1, 2, 3, 3, 3, 2, 1]
               |
               |______
                      |
                      |
                      V
index        0  1  2  3
represents   0  1  2  3
            [0, 2, 5, 7]
                      |
                      |________   # (7 - 1)
                               |
                               |
                               V
             0, 1, 2, 3, 4, 5, 6
            [0, 0, 0, 0, 0, 0, 3]

    8. Copy the sorted array to the original array
    '''
    # 1 -- 
    length = len(arr)
    output = [0] * length
    # 2 --
    counts_length = 0
    if maximum :
        counts_length = int(maximum) + 1
    else:
        counts_length = 1
    counts = [0] * (counts_length)
    # 3 --
    for index in range(0, length):
        # 4 --
        # 4.1
        value = arr[index]
        #4.2
        counts[value] += 1
    # 5 --
    for index, value in enumerate(counts):
        # 6 --
        if index > 1:
            previousIndex = index - 1
            value += arr[previousIndex]
        else:
            value = value
    # 7.1 --
    for index, value in enumerate(arr):
        # 7.2 --
        value_index = counts[value]
        # 7.3 --
        counts[value] -= 1
        #7.4 --
        output[counts[value]] = value_index
    # 8 --
    for index in range(0, length):
        arr[index] = output[index]
