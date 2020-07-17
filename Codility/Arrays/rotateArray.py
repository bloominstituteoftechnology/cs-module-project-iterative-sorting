def solution(A, K):
    # write your code in Python 3.6
    # newArray = [0 for _ in A]
    # print(newArray)
    # length = len(A) - 1
    
    # for i in range(0, len(A)):
    #     if (i + K) <= length:
            
    #         newArray[i+K] = A[i]
    #     else:
    #         index = i + K - len(A)
    #         newArray[index] = A[i]
    # return newArray
    if len(A) <= 1:
        return A
    #rotate 1 by 1
    while K > 0:
        newArray = [0 for _ in range(len(A))]
        for i in range(len(A)):
            if i < len(A) - 1:
                print('i', i)
                print('newArray', newArray)
                newArray[i + 1] = A[i]
            if i == len(A) - 1:
                newArray[0] = A[i]
        K = K -1
        print(newArray)
        A = newArray
        print(A)
    return A


#print(solution([9,3,4,2,4, 90, 89], 5))

i = 4
length = 5
K = 23



def solution1(A, N):
    #number of times to rotate
    #for each time, rotate once, until required times
    # if not the last number, rotate 1 position
    # put last number to 0 position
    #while N is > 0
    
    
    while N > 0:
        rotator = [0 for _ in range(len(A))]
        for i in range(len(A)):
            if i < len(A) - 1:
                print('>', i)
                rotator[i+1] = A[i] 
                #A[i+1] = A[i]
            elif i == len(A)-1:
                print('==', i)
                rotator[0] = A[i]
                #A[0] = A[i]
            print(rotator)
            print('A',A)
        N -= 1
        A = rotator
        print(rotator)
        print('A',A)
    return rotator


print(solution1([9,3,4,2,4, 90, 89], 2))