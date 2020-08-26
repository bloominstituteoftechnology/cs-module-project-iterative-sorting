# TO-DO: Complete the selection_sort() function below
def insertion_sort(arr):
    # loop through n-1 elements
    # first element is already in the sorted side

    # for all other items, we should do things
    # starting at the second item, iterate until the end of the array
    for i in range(1, len(arr)):
        # the current number at the index represents the value currently being sorted
        current = arr[i]
        # move the current number back through the array (to the sorted side)
        j = i
        # keep moving until: its greater than the number before it OR we reache the start of array

        # *this loop is a linear loop
        while j > 0 and current < arr[j-1]:
            # replace current value and the one to the left of it, swap them
            arr[j] = arr[j-1]
            j -= 1
        # set value at the current index to the current number
        # j is the val we kept looping to the left of -> it ends bc its at the end, or bc there are smaller val to the left
        # j reps the correct new location fot the current number
        arr[j] = current

    return arr


arr = [64, 12, 31, 2, 67, 30, 59, 89, 76, 95, 58, 1, 94, 22, 41]
print(insertion_sort(arr))
