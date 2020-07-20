# Insertion Sort:

def insertion_sort(input_list):
    # Separate the first element and
    # think of it as sorted
    # no code required / abstract step

    # For all unsorted items
    for i in range(1, len(input_list)):
        # Mark the current item we are considering
        current_value = input_list[i]
        # look left until we find the correct place to
        # insert the current_value
        j = i
        while j > 0 and current_value < input_list[j-1]:

            # As we are looking left we need to shift items to the right
            input_list[j] = input_list[j-1]
            j -= 1

        # When we have found our insertion point (j)
        # insert item
        input_list[j] = current_value

    return input_list
