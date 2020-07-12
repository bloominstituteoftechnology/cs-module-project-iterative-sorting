#algo to find greatest common denominator
def euc(A,B):
    low = min([A,B])
    high = max([A,B])

    if low == 0:
        return high

    low = high%low
    high = B
    print('high',high)
    return euc(high, low) 
    




A = 10
B = 14
print(euc(A,B))