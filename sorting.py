


# O(n)

def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
    return -1


# worst case,this function takes n amount of operations to complete
# this is why the above example is linear time or O(n)

arr = [0, 1, 2, 3, 4, 5, 98, 99]

# if an array is sorted it makes it much easier to find the correct value!




arr = [99, 98, 5, 2, 3, 1, 0, 4]
current_element = 4

# Insertion Sorting Pseudo-Code
def insertion_sort(arr):
# Start with looping at the second element
    for idx in range(1, len(arr)):
# pick up the current element and hold it
        current_element = arr[idx]
        current_idx = idx
# while current element is less than its left
        while current_idx > 0 and current_element < arr[current_idx - 1]:
# copy left and move it on the right
            arr[current_idx] = arr[current_idx - 1]
# decrement the index so that it moves along the list
            current_idx -= 1
# finally, put the current element down
        arr[current_idx] = current_element

# arr[i], arr[i -1] = arr[i -1], arr9[i]

insertion_sort(arr)
print(arr)

# time complexity of insertion sort 
# n * ( 1 + 1 + (n * 2) + 1)
# n * (n**2)
# n**2 is the largest factor
# O(N**2) runtime, or quadratic.