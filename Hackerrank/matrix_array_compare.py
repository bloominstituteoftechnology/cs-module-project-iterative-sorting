#given a matrix 3 x 3
# compute the absolute difference between diagonial sums

def diagonalDifference(arr):
    d1 = 0
    d2 = 0 
    n = 3

    #solve d1
    
    for i in range(0, n-1):
        d1 += arr[i][i]
    #range([start], stop[, step])
    
    for i in range(n-1, -1):
        d2 += arr[i][i]
    
    return d2 - d1 

print(diagonalDifference(arr))