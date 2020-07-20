def selection_sort(items):
    for i in range(0, len(items) - 1):
        current_index = i
        smallest_index = current_index
        for j in range(current_index + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j
            items[smallest_index], items[current_index] = items[current_index], items[smallest_index]

    return items


our_numbers = [5, 9, 3, 6, 2, 1, 7, 8, 4]

print(selection_sort(our_numbers))
