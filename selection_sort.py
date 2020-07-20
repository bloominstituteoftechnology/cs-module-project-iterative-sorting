# def selection_sort(items):
#     for i in range(0, len(items) - 1):
#         current_index = i
#         smallest_index = current_index
#         for j in range(current_index + 1, len(items)):
#             if items[j] < items[smallest_index]:
#                 smallest_index = j
#             items[smallest_index], items[current_index] = items[current_index], items[smallest_index]

#     return items


# our_numbers = [5, 9, 3, 6, 2, 1, 7, 8, 4]

# print(selection_sort(our_numbers))

# def selection_sort(list_to_sort):
#     for i in range(0, (len(list_to_sort) - 1)):
#         min_index = i
#         for j in range((i+1), len(list_to_sort)):
#             if list_to_sort[j] < list_to_sort[min_index]:
#                 min_index = j
#             if min_index != i:
#                 list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]
#     return list_to_sort


# new_numbers = [9, 7, 3, 6, 1, 4, 0, 5, 2, 8]

# print(selection_sort(new_numbers))


def selection_sort(list_to_sort):
    for i in range(0, len(list_to_sort) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(list_to_sort)):
            if list_to_sort[smallest_index] > list_to_sort[j]:
                smallest_index = j
        current = list_to_sort[cur_index]
        list_to_sort[cur_index] = list_to_sort[smallest_index]
        list_to_sort[smallest_index] = current

    return list_to_sort


new_numbers = [9, 7, 3, 6, 1, 4, 0, 5, 2, 8]

print(selection_sort(new_numbers))
