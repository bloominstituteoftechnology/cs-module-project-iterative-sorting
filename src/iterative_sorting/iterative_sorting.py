# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        swap_holder = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = swap_holder
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap_holder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = swap_holder
                swaps += 1
        


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
