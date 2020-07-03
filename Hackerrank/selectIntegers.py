def count_div(A, B, K):
    # '''
    # Returns the number of integers within the range [A..B] that are divisible by K.
    # 
    # Used generators to save memory on large amounts of data.
    
    count = 0
   

    for x in range(A, B + 1):
        print(x)
        if (x % K) == 0:
            count += 1
    return count

print(count_div(1, 10, 2))





arr = [3,4,5,2,5,2,3]

count_div
