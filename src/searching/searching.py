import sys 
sys.path.append("../insertion_sorting")
from insertion_sort import insertion_sort

def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    sorted_arr = insertion_sort(arr)
    lowest_index = 0
    highest_index = len(sorted_arr) - 1
    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        if sorted_arr[middle_index] == target:
            return middle_index
        if sorted_arr[middle_index] > target:
            highest_index = middle_index - 1
        if sorted_arr[middle_index] < target:
            lowest_index = middle_index +1
    return -1  # not found


if __name__ == "__main__":
    binary_search([1,2,3,4,5,6,7], 10)