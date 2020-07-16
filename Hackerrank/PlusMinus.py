def plus_minus(D, A):
    #print to number of decimals
    #find ratio of pos, neg and 0
    #get sum
    total_len = len(A)
    pos = []
    neg = []
    zero = []
    for x in A:
        if x > 0:
            pos.append(x)
        if x < 0:
            neg.append(x)
        if x == 0:
            zero.append(x)
    posR = len(pos)/total_len
    
    print(format(posR, '.6f'))
    print(format(len(neg)/total_len, '.6f'))
    print(format(len(zero)/total_len, '.6f'))
    
    #print('{0:.%df}'.format(posR)) % (D)
    

D = 6
A = [-4,3,-9,0,4,1]
plus_minus(D, A)
