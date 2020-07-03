#https://gist.github.com/1st/5278729
def triangle(A):
    '''
    Calculate triangel of integers, where sentense of numbers P, Q, R
    correspond to next rules:
     - P + Q > R
     - Q + R > P
     - R + P > Q
    Args:
      - A: list of integers, where we will search triangle
    Return: 1 - if triangle exists, and 0 - otherwise
    '''
    count = 0
    arr = []
    for P in range(0, len(A)):
        for Q in range(0, len(A)):
            for R in range (0, len(A)):
                print('P', P, 'Q', Q,'R', R)
                if P != Q and Q != R and P != R:
                    if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]:
                        return 1
    return 0


#Option 2
def triangle1(A):
    A = tuple(enumerate(A))
    for p, P in A:
        #print(p, A)
        for q, Q in A[p + 1:]:
            #print(q, Q)
            for r, R in A[q + 1:]:
                #print(r, R)
                if (P + Q > R) and (Q + R > P) and (R + P > Q):
                    arr.append([P,Q,R]) 
    
        
    
A = [1,2,3,4]
print(triangle1(A))



#Option 3
def triangle2(A):
    pools=tuple(A)*3
    n=len(pools)
    result=[[]]
    for pool in pools:
        result=[x+[y] for x in result for y in pool]
    for prod in result:
        if len(set(prod))==3:
            R=prod[0]
            P=prod[1]
            Q=prod[2]
            if P+Q>R and Q+R>P and R+P>Q:
                return 1
    return 0
print(triangle2([[10, 2, 5, 1, 8, 20]]))