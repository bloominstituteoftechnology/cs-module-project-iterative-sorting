# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# For example, . Our minimum sum is  and our maximum sum is . We would print

# 16 24

def min_max(arr):
    #min sum in the array
    #max sum in the array
    #make a new array with sums
    
    arr.sort()
    
    #print(sorted)
    arrSum = [arr[0]]
    previous = arr[0]
    for i in range(len(arr)-1):
        arrSum.append(previous+arr[i+1])
        previous += arr[i+1] 
    total = arrSum[-1]
    print(total - arr[-1], total - arr[0])
    

A = [7, 69, 2 ,221 ,8974]
print(min_max(A))

def min_max1(arr):
    #min sum in the array
    #max sum in the array
    #make a new array with sums
    
    arr.sort()
    
    #print(sorted)
    arrSum = sum(arr)
    
    print(arrSum - arr[-1], arrSum - arr[0])
    

A = [7, 69, 2 ,221 ,8974]
print(min_max1(A))