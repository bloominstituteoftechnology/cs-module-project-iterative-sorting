# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for items in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[items]:
                smallest_index = items


        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for each in range(0, len(arr)-1):
        for item in range(0, len(arr) - each - 1):
            if arr[item] > arr[item + 1]:
                arr[item], arr[item + 1] = arr[item + 1], arr[item]


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
