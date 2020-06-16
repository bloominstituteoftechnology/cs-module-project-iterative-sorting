#divide and conquer
# split work, and have it worked on in parallel in smaller chucks
# quicksort
# find a pivot.  
# pick pivot
#2. divide data to left or right of pivot
#3 then pick another pivot for divided groups

def partition(data):
    #pick first element in data as the pivot
    pivot = data[0]
    left = []
    right = []
    #slice, take every item but first, which is pivot
    for x in data[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    print('left', left, 'pivot', pivot, 'right', right)
    return left, pivot, right
def quicksort(data):
    #recursive
    #1. what is base/terminating case?
    #2. if not in base case, how are moving towards base case(s)
    #base case

    #get rid of empty left or right lists
    if len(data) == 0:
        return data
    print(data)
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)

arr = [1,4,2,2,9,12,1,4,50, 32]

print(quicksort(arr))


# instead of using partition, can make more memory efficient
# by not creating new left and rights
def newPartition(data, start, end):
    pivot = data[start]

    i = start + 1
    j = start + 1

    while j <= end:
        if data[j] <= pivot:
            #swap
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1
    
    data[start], data[i-1] = data[i -1], data[start]
    return i - 1

 

def quicksort2(data, start=0, end=None):
    #get lenght of data
    if end is None:
        end = len(data) - 1

    #base case, data has already be sorted
    if len(data) == 0:
        return data

    #returns the index of the pivot
    # and partitions of data around pivot
    index = newPartition(data, start, end)

    #quicksort everything to left of pivot
    quicksort2(data, start, index - 1)
    #quicksort everything to right of pivot
    quicksort2(data, index + 1, end)

# print(quicksort2(arr))