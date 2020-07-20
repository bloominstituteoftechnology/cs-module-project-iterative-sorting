def solution(A, S):
    length = len(A)

    p1 = 0
    count = 0
    for i in range(len(A)):
        pointer = i
        p1 = i
        #print('i',pointer)
        while p1 < len(A):
            print('i', pointer,'p1+1', p1+1, A[pointer: p1+1])
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


def solution1(A, S):
    #consecutive values, whose average is S

    
    count = 0
    for i in range(len(A)):
        i
        p1 = 0
        #print('i',pointer)
        while p1 < len(A):
            # print('i', i)
            # print(A[p1])
            amount = sum(A[i: p1+1])
            #print(amount)
            numD = len(A[i: p1+1])
            print('amount',amount, 'numD',numD)
            if amount > 0 and amount/numD == S:
                count += 1
                print(count)
            p1 += 1
    return count


S = 0
A = [0,0,0]
print(solution1(A, S))


def solution2(A, S):
    #consecutive values, whose average is S

    
    count = 0
    for i in range(len(A)):
        i
        p1 = 0
        #print('i',pointer)
        while p1 < len(A):
            # print('i', i)
            # print(A[p1])
            amount = sum(A[i: p1+1])
            #print(amount)
            numD = len(A[i: p1+1])
            print('amount',amount, 'numD',numD)
            if amount > 0 and amount/numD == S:
                count += 1
                print(count)
            p1 += 1
    return count


S = 0
A = [2,1,3]
print(solution2(A, S))