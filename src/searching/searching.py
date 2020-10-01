def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    first = 0
    last = (len(arr) - 1)
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        print(f"The middle is {middle}")
        
        # check to see if item is the middle target
        print(f"The middle is {arr[middle]} and the target is {target}")
        if target == arr[middle]:
            print("found value")
            found = True
            return middle
        # else check to see if the number is smaller or larger and repeat
        else:
            print("Target not found so going through the else ")
            if target < arr[middle]:
                # if smaller change the last number to be the middle
                last = middle - 1
                print("changed last")
            else:
                first = middle + 1
                print("changed first")
        
    return -1

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
binary_search(arr1, -8)
