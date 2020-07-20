def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, right, pivot


def quicksort(data):
    if data == []:
        return data

    left, right, pivot = partition(data)

    return quicksort((left) + [pivot] + (right))
