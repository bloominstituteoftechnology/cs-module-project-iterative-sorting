def quicksort(a):
    def quicksort_recursive(a, low, high):
        if low >= high:
            return

        p = low  # Pivot index

        # Partition step

        for i in range(low, high):
            if a[i] < a[p]:
                # Swap element i with item to right of pivot
                a[p + 1], a[i] = a[i], a[p + 1]

                # Swap pivot with element on its right
                a[p + 1], a[p] = a[p], a[p + 1]

        # At this point, the pivot is in its final spot, and the left and right
        # partitions need to be sorted

        quicksort_recursive(a, low, p)
        quicksort_recursive(a, p + 1, high)

    quicksort_recursive(a, 0, len(a))


a = [-5, 9, 3, -7, 15, 8, 1, 19]

quicksort(a)

print(a)
