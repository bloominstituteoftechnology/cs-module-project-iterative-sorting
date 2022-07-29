def solution(A):
    counts = {}
    #loop through nums to tally up how many times we've seen each number
    for x in A:
        if x in counts:
            #remove
            counts.pop(x)
        else:
            counts[x] = 1
    #loop through all key-value pairs in counts to find the one pir
    #whose value is 1
    for num in counts:
        return num
      

arr = [9,3,9,3,9,7,9]
print(solution(arr))


def solution1(A):
    maxValue = max(A)
    if len(A) == 1:
        return A[0]
    
    elements = [0 for _ in range(0, maxValue + 1)]
    for x in A:
        if elements[x] == x:
            elements[x] = 0
            
        else:
            elements[x] = x
    return sum(elements)        
    

arr = [9,3,9,3,9,7,9]
print(solution1(arr))

