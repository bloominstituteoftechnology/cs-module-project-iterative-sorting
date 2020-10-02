import math


def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # declare the start/ middle /end of the array
    middle_index = math.ceil(len(arr)/2 - 1)
    start_index = 0
    end_index = len(arr) - 1
    # compare middle against target
    # loop until start crosses end
    while start_index < end_index:
        # if equal, stop
        if arr[middle_index] == target:
            return middle_index
        # if greater pick the mid of the right half
        elif arr[middle_index] > target:
            end_index = middle_index - 1
            middle_index = math.ceil((start_index + end_index) / 2)
        # if less pick the mid of the left half
        elif arr[middle_index] < target:
            start_index = middle_index + 1
            middle_index = math.ceil((start_index + end_index) / 2)
    return -1  # not found
