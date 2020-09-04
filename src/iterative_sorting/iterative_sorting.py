# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for smallest_index in range(i+1, len(arr)):
            if arr[smallest_index] < arr[cur_index]:
                cur_index = smallest_index

        arr[i], arr[cur_index] = arr[cur_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
