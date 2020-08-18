'''
cs32
'''
def insertion_sort(input_list):
    # think of the first element as sorted

    # for all unsorted items
    for i in range(1, len(input_list)):
        # mark the current item we are considering
        current = input_list[i]

        # look left until we find the proper
        # place to insert the current item
        j = i
        while j > 0 and current < input_list[j-1]:
            # as we are "looking left", we need to
            # shift items to the right
            input_list[j] = input_list[j-1]
            j -= 1

        # when we've found our insertion point (j)
        # insert item
        input_list[j] = current

    return input_list

print(insertion_sort([9,8,7,6,5,4,3,2,1]))



'''
cs34
'''
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
