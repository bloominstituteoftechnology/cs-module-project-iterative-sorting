def linear_search(arr, target):
    # Your code here

    #print(f'array {arr}')
    #print(f'target{target}')

    for item in arr:
       # print(item)
        #print(f'arr index {arr.index(item)}')
        if item == target:
           # print(f'FOUND THE NUMBER {item} at position {arr.index(item)}')
            return arr.index(item)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    
    first_index = 0
    last_index = (len(arr)-1)
    middle_index = (first_index + last_index) // 2

    print(f'first index {first_index}')
    print(f'last index {last_index}')
    print(f' middle index {middle_index}')
    print(f'target {target}')
    print(f'OG arr {arr}')

    lookup_arr = arr

    ## if target IS the middle index, return middle index
    
    
    while len(arr) >= 1:
        print(f'array at middle index {arr[middle_index]}')
        if target == arr[middle_index]:
            print(f'!!!!!!!!!middle index {middle_index}')
            return middle_index

        elif target < arr[middle_index]:
            last_index = middle_index
            middle_index = (first_index + last_index) // 2
            arr = arr[0:last_index]
            print(arr)
    
    #if len(arr) == 1 and searching_arr[0] == target:
    #     return arr.index(target)
    
    return -1













    # searching_arr = arr

    # while (len(searching_arr) > 1):

    #     if (target == middle_item):
    #         return searching_arr.index(middle_item)
            
    #     elif target < middle_item:
    #         print('target is less than middle')
    #         searching_arr.index(last_item) = searching_arr.index(middle_item) - 1
    #         print(last_item)
    #         print(searching_arr.index(last_item))
    #         # searching_arr = searching_arr[0:searching_arr.index(last_item)]
    #         print(searching_arr)
        
    #     elif target > middle_item:
    #         print('target is more than middle')
    #         first_item = middle_item + 1
    #         searching_arr = searching_arr[first_item:last_item]
    #         print(searching_arr)

    #     print(searching_arr)
    # if len(searching_arr) == 1 and searching_arr[0] == target:
    #     return arr.index(target)


    # return -1  # not found

    # while len(arr) > 1:

    #     if (target == middle_item):
    #         return arr.index(middle_item)
        
    #     elif target < middle_item:
    #         last_item = middle_item - 1
    #         arr = arr[first_item:last_item]
        
    #     elif target > middle_item:
    #         first_item = middle_item + 1
    #         arr = arr[first_item:last_item]

    #     print(arr)
    # if len(arr) == 1 and arr[0] == target:
    #     return arr[0]


