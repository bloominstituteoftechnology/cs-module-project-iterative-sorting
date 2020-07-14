def solution(T,R):
    if 'OK' not in R:
        return 0

    if R.count('OK') == len(R):
        return 100
    arrT = []
    total = []
    for x in T:
        arrT.append(x[4:])
    for x in arrT:
        total.append(x[0:1])
    num_test = len(set(total))
    notOK = []
    for i in range(len(R)):
        if R[i] != 'OK':
            notOK.append(i)
    #print(notOK)
    notOkTest = []
    for i in range(len(total)):
        if i in notOK:
            notOkTest.append(total[i])
    #print('num', num_test, 'not', len(set(notOkTest)))
    passed = num_test - len(set(notOkTest))
    #print(passed)
    return int((passed * 100) / num_test)
            

        # for j in range(len(total)):
        #     if 
    




R = ['Wrong answer', 'OK', 'Runtime error', 'OK', 'Time limit exceeded']
T = ['test1a', 'test2', 'test1b', 'test1c', 'test3']
print(solution(T,R))