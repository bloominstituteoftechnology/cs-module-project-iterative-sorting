# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # establishes first index
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] <= arr[smallest_index]:
                smallest_index = j
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]



        # TO-DO: swap
        # Your code here

    return arr

#list = [1,4,6,3,7,0,9,8]
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                swapped = True
    



    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
