def insertionSort1(n, arr):
    temp = arr[n-1]
    previous = n-2
    position = n-1
    while temp < arr[previous]:
        arr[position] = arr[previous]
        previous -= 1
        position -= 1
        print(*arr)
    arr[position] = temp
    print(*arr)

arr = [2, 4, 6, 8, 3]
n = 5
print(insertionSort1(n, arr))