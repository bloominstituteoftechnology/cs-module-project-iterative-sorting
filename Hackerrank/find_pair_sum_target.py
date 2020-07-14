def pair(A,B,T):
    closest = abs(T-(A[0]+B[0]))
    pair = {'A':A[0], 'B':B[0]}
    print('pair', pair)
    for x in A:
        for j in B:
            value = abs(T-(x+j))
            if value < closest:
                closest = value
                pair = {'A':x, 'B':j}
    return closest, pair



A = [-1, 3, 8, 2, 9, 5]
B = [4, 1, 2, 10, 5, 20]
T = 24
print(pair(A,B,T))


def pair1(A,B,T):
    
   
    for x in A:
        if T-x in B:
            return [x, T-x]
        
    return 'not found'


A = [-1, 3, 8, 2, 9, 5]
B = [4, 1, 2, 10, 5, 20]
T = 24
print(pair1(A,B,T))

