def solution(A, S):
    length = len(A)

    p1 = 0
    count = 0
    for i in range(len(A)):
        pointer = i
        p1 = 0
        #print('i',pointer)
        while p1 < len(A):
            amount = sum(A[pointer: p1+1])
            numD = len(A[pointer: p1+1])
            #print('amount',amount, 'numD',numD)
            if amount > 0 and amount/numD == S:
                count += 1
                #print(count)
            p1 += 1
    return count


S = 2
A = [2,1,3]
print(solution(A, S))