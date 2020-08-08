# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # swapping
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr


def bubble_sort(arr):
    for i in range(len(arr)-1):
    # 1st loop through 0 to n - 1 of array (0 to 9)
    # 2nd loop thru 1 to 9
        for j in range(0, len(arr) - i - 1):
        #1st outter
            # 1st inner loop through 0 to (10 - 0 - 1) = 9
            # 2nd inner loop 1 thru 9
            # 3rd inner loop 2 thru 9 etc...
        #2nd outter
            # 1st inner loop through 1 to (10 - 1 - 1) = 8
            # 2nd inner loop 2 thru 8 etc...
            if arr[j] > arr[j+1]:
                # 1st if arr[0] > arr[1] -> swap
                # 2nd if arr[1] > arr[2] -> swap etc...
                # swapping
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
    # create array for holding counts
    count_arr = [0 for i in maximum + 1]

    # count elements in the array
    for i in arr:
        count_arr

    # assign count to indexes in count_arr



    return arr

"""
def countSort(arr):
    # The output character array that will have sorted arr 
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul 
    # characters and initialize count array as 0 
    count = [0 for i in range(256)]

    # For storing the resulting answer since the  
    # string is immutable 
    ans = ["" for _ in arr]

    # Store count of each character 
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(256):
        count[i] += count[i - 1]

        # Build the output character array 
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans
"""

# insertion_sort
my_list = [8, 2, 5, 4, 1, 3]

# left of the line is sorted, right is not
# my_list = [8, | 2, 5, 4, 1, 3]

# remove 2 and insert in front of 8
# temp = 2
# my_list = [2, 8, | 5, 4, 1, 3]

# remove 5 and insert in front of 8 and after 2
# temp = 5
# my_list = [2, 5, 8, | 4, 1, 3]

# separate the first element, think of it as sorted
# for all other items, starting at the second (index 1)
    # put current num into temp var
    # look left, until we find correct position
    # as we look left left, shift items to right
# when left is smaller than temp or we're at zero index, put at this location

def insertion_sort(list_to_sort):
    # separate the first element, think of it as sorted
        # no code -- abstract idea
    # for all other items, starting at the second (index 1)
    for i in range(1, len(list_to_sort)):
        # put current num into temp var
        temp = list_to_sort[i]
        # look left, until we find correct position
        j = i
        while j > 0 and temp < list_to_sort[j-i]:
            print(j)
            # as we look left left, shift items to right
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        # when left is smaller than temp or we're at zero index, put at this location
        list_to_sort[j] = temp
    return list_to_sort

print(insertion_sort(my_list))