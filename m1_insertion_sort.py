# O(n)
def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
    return -1

# find_num(arr, 99)

arr = [0, 1, 2, 3, 4, 5, 98, 99]



arr = [98, 99, 5, 2, 3, 1, 4, 0]
# Pseudocode for insertion sort
# Insertion sort works in place
def insertion_sort(arr):
    ## start looping at the second element
    for idx in range(1, len(arr)):
    ## pick up the current element and hold it
        current_element = arr[idx]
        current_idx = idx
    ## while current element is less than its left sibling
        while current_idx > 0 and current_element < arr[current_idx - 1]:
        ### copy left sibling to the right
            arr[current_idx] = arr[current_idx - 1]
            ### decrement index
            current_idx -= 1
    ## finally, put our current element down
        arr[current_idx] = current_element

        
# n * (1 + 1 + (n * (1 + 1)) + 1)
# n * (3 + (n * 2))
# n * (3 + 2n)
# 3n + 2n^2
# n + n^2
# O(n^2)


# time complexity of insertion sort?
# n * (1 + 1 + (n * 2) + 1)
# n * (3 + 2n)
# 3n + 2n^2
# O(n + n^2)
# O(n^2)



# arr[i], arr[i - 1] = arr[i - 1], arr[i]

insertion_sort(arr)
print(arr)