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


def insertion_sort_2(input_list):
    # start at index 1 to consider the fist item "sorted"
    # current value will be the actual value in the list
    # during that iteration
    # note that i starts at 0 (even though we are starting 
    # at the 1st index)
    for i, current in enumerate(input_list[1:]):
        
        # add 1 to j to represent the actual index we are 
        # at in the array
        j = i + 1
        
        # check to see if we are at the beginning of the list
        # and if the value to the left of current is greater than
        # current
        while j > 0 and current < input_list[j-1]:
            # current is smaller:
            # move things to the right... 
            # keep doing this until we get to the beginning
            # of the list OR the left value is smaller than
            # current
            input_list[j] = input_list[j-1]
            j -= 1

        # assign the current value to wherever j was when the loop
        # ended
        input_list[j] = current

    return input_list

print(insertion_sort_2([9,8,7,6,5,4,3,2,1]))




            
