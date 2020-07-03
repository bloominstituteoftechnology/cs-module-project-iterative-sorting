def sortLetters(s):
    #put string in array
    arr = []
    for x in s:
        arr.append(x)
    
    for i in range(0, len(arr)):
    #point to current and previous values
        current = i
        previous = i-1
        while previous >= 0 and arr[current] < arr[previous]:
            #swap
            arr[previous], arr[current] = arr[current], arr[previous]
            #after swap select the 2 to the left
            current -= 1
            previous -= 1
    return ''.join(arr)
s = 'ABNANSDA'
print(sortLetters(s))