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


print(solution([9,3,4,2,4, 90, 89], 5))

i = 4
length = 5
K = 2
        