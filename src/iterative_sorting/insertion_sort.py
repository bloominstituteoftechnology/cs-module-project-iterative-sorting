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
