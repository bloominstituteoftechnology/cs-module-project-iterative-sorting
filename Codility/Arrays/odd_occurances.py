def solution(A):
    # write your code in Python 3.6
    maxValue = max(A)
    #maxValue + 1, because starts with 0
    elements = [0 for _ in range(0, maxValue + 1)]
    
    print(elements)
    for i in A:
        elements[i] += 1
    print(elements)
    for i in range(len(elements)):
        if elements[i] == 1:
            odd = i
    return odd
print(solution(arr))