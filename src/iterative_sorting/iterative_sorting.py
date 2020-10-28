# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements

    for i in range(len(arr)):
        # print(f"i is: {i} ")
        cur_index = i
        for j in range(i+1, len(arr)):
            # print("here....")
            # print(f"cur_index: {cur_index} ->el: {arr[cur_index]} ")
            # print(f"j is: {j} ->el: {arr[j]} ")
            if arr[cur_index] > arr[j]:
                cur_index = j
        arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr

array = [1,5,9,4,2,7,0,1,100,99,101]
# print(f"result is: {selection_sort(array)} ")


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr)
    print(f"---------array: {arr} ")
    print(f"n is {n} ")
    for i in range(n):
        swapped = False
        print(f"==========i is: {i}================ ")
        for j in range(0, n-i-1):
            print(f"j is: {j} ")
            if arr[j] > arr[j+1]:
                print(f"---------j is: {j} el: {arr[j]} el+1: {arr[j+1]} ")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"_________runningArray: {arr} ")
                swapped = True
        if swapped == False:
            break
    return arr

print(f"result is: {bubble_sort(array)} ")


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


Array:  [1, 4, 1, 2, 7, 5, 2]

1. Count the indexes in given array:

Index:      0 1 2 3 4 5 6 7 8 9
Count:      0 2 2 0 1 1 0 1 0 0

2. sum the count array with previous

Index:      0 1 2 3 4 5 6 7 8 9
Count:      0 2 4 4 5 6 6 7 7 7




'''


def counting_sort(arr, maximum=None):
    # Your code here
    maximum = 0
    minimum = 0

    if len(arr) > 0:
        # why I didn't have to use global here
        maximum = int(max(arr))
        minimum = int(min(arr))

    size = len(arr)
    print(f"max: {maximum} minimum: {minimum} size: {size} ")
    if minimum < 0:
        return 'Error, negative numbers not allowed in Count Sort'

    count = [0 for _ in range(maximum+1)]
    # update count array with counting each element in from the array
    for i in range(size):
        count[arr[i]] += 1

    print(f"count is: {count} ")

    # update position in count array by adding count[i] = count[i] + count[i-1]
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    # create output array and fill in the position
    output = [0 for _ in range(size)]
    print(f"count is: {count} ")

    while size > 0:
        pos = count[arr[size-1]]
        print(f"size: {size} pos: {pos} arr[i]: {arr[size-1]} ")
        output[pos-1] = arr[size-1]
        print(f"output: {output} ")
        count[arr[size-1]] -= 1
        size -= 1

    return output


arr1 = [1, 5, 8, 8, 4, 2, 9, 6, 0, 3, 7]
print(counting_sort([]))


# print('challenge: ')
# Print out all of the numbers in the following array that are divisible by 3:


myArray = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]


def divisible_by_three(arr):
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            # print(arr[i])
            pass


divisible_by_three(myArray)

'''
27
81
8
27
99
63
42
'''
