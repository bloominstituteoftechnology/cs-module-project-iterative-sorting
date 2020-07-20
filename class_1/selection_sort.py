# runtime: O(n * n) = O(n^2)
def selection_sort(arr):
    # Iterate through the array (represents the sorted-unsorted
    # boundary moving across the array)
    for i in range(len(arr)): # O(n)
        # index of the boundary, as well as the index we're
        # going to swap the smallest element with
        boundary = i

        smallest_value = arr[boundary]
        smallest_index = boundary
        # finding the smallest element
        # in the "unsorted" portion of the array (right side)
        for unsorted_index in range(boundary, len(arr)): # O(n)
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index


        # `smallest` is the smallest element in the unsorted
        # portion

    
        # Once that's found, swap it with the elem on the right 
        # edge of the sorted-unsorted boundary
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]

    return arr

if __name__ == "__main__":
    arr = [5, 55, 6, 67, 16, 9, 25, 43, 12]
    print(selection_sort(arr))