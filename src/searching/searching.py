def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # variables to store the min and max of the remaining searchable portion of array
    min_position = 0
    max_position = len(arr)
    print(f"min: {min_position}, max: {max_position}")
    # Iterates through search until it finds the value
    for _ in range(0, (len(arr)//2)):
        # Variable to store the currently tested position in the array
        new_position = (max_position + min_position) // 2
        print(f"new position: {new_position}")

        # If the value at new_position is the target, return the value
        if arr[new_position] == target:
            return new_position # target found

        # Otherwise, if the value is less than the target, set min to new position for the next loop
        elif arr[new_position] < target:
            min_position = new_position
            print(f"min: {min_position}, max: {max_position}")

        # lastly, if value is greater than the target, set max to new position for the next loop
        else:
            max_position = new_position
            print(f"min: {min_position}, max: {max_position}")

    return -1  # not found
