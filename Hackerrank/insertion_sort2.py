#sort an existing array, starting at position 0

def insertionSort2(n, arr):
    
    #compare element to all previous elements
    #when find a smaller element insert into position
    for i in range(1, n):
        element = i
        position = i-1
        while position >= 0 and arr[element] < arr[position]:
            arr[position], arr[element] = arr[element], arr[position]
            position -= 1
            element -= 1
        print(*arr)
n = 6
arr = [1, 4, 3, 5, 6, 2]

    
#print(insertionSort2(n, arr))


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        current = i
        while (j >= 0) and (l[current] < l[j]):
           l[current], l[j] = l[j], l[current]
           j -= 1
           current -= 1
    return l

n = 6
l = [7, 4, 3, 5, 6, 2]
print(insertion_sort(l))