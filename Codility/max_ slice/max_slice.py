def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        print(a, max_ending)
        print(max_slice, max_ending)
        max_slice = max(max_slice, max_ending)
    return max_slice
    
A = [3,2,6,-1,4,5,-1,2]
print(golden_max_slice(A))