def runningTime(arr):
    shifts = 0
    for i in range(1, len(arr)):
        print('print i',i)
        current = i
        previous = i - 1

        while previous >= 0 and arr[current] < arr[previous]:
            shifts += 1
            arr[current], arr[previous] = arr[previous], arr[current]
            print(arr)
            previous -= 1
            current -= 1
            
            print('increase shift')
    return shifts

    
arr = [2, 1, 3, 1, 2]
print(runningTime(arr))