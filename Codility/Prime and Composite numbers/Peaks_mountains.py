# A non-empty array A consisting of N integers is given.

# A peak is an array element which is larger than its neighbours.
#  More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

# For example, the following array A:

#     A[0] = 1
#     A[1] = 5
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# has exactly four peaks: elements 1, 3, 5 and 10.

# You are going on a trip to a range of mountains whose relative heights
#  are represented by array A, as shown in a figure below. You have to choose
#  how many flags you should take with you. The goal is to set the maximum number
#  of flags on the peaks, according to certain rules.



# Flags can only be set on peaks. What's more, if you take K flags, 
# then the distance between any two flags should be greater than or equal to K.
#  The distance between indices P and Q is the absolute value |P − Q|.

# For example, given the mountain range represented by array A, above, with N = 12, if you take:

# two flags, you can set them on peaks 1 and 5;
# three flags, you can set them on peaks 1, 5 and 10;
# four flags, you can set only three flags, on peaks 1, 5 and 10.
# You can therefore set a maximum of three flags in this case.

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the maximum number of flags 
# that can be set on the peaks of the array.

# For example, the following array A:

#     A[0] = 1
#     A[1] = 5
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# the function should return 3, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..400,000];
# each element of array A is an integer within the range [0..1,000,000,000].

def peak(A):
    
    if len(A) == 0:
        return 0
    #find peaks, and where
    arr = [0 for _ in range(len(A))]

    for i in range(1, len(A)):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            arr[i] = 1
    peaks = sum(arr)
    first = -1
    #print('arr', arr)
    if sum(arr) == 1:
        return 1
    if sum(arr) < 1:
        return 0
    while first == -1:
        for i in range(len(arr)):
           
            if arr[i] == 1:
                
                first = i
                break
    
    newM = [0 for _ in range(len(A))]
    newM[first] = 1
    
    #set flags back on mountain
    for i in range(first + 1, len(arr)):
        no = i-peaks+1
        print('no', no)
        # print('no arr', arr[no: i])
        # print('i', i)
        if arr[i] == 1 and i > no and sum(arr[no: i]) == 0:
            print('put flag')
            print('newM i', i)
            newM[i] = 1
            print(newM)
        elif arr[i] == 1 and sum(arr[no: i]) > 0:
            arr[i] = 0
           

    return sum(newM)
        
    
    # return sum(arr)
        


                    


    #print(arr)


A = [1,5,3,4,3,4,1,2,3,4,6,2]
#print(peak(A))


def peak1(A):
    if len(A) == 0:
        return 0
    #find peaks, and where
    arr = [0 for _ in range(len(A))]
    print(sum(arr))
    

    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            arr[i] = 1
    peaks = sum(arr)
    
    if sum(arr) == 1:
        return 1
    if sum(arr) < 1:
        return 0
    
    
    print('arr', arr)
    p1 = 0
    p2 = len(arr)-1
    flags=0
    while p1 < p2:
        print(arr[p1], p1, arr[p2], p2)
        if arr[p1] == 1 and arr[p2] == 1 and p2-p1 >= peaks:
            flags += 2
            p1 += flags
            p2 -= flags
        elif arr[p1] == 1 and arr[p2] == 1 and p2-p1 < peaks:
            flags += 1
            break
        elif arr[p1] == 1 and arr[p2] == 0:
            p2 -= 1
        elif arr[p1] == 0 and arr[p2] == 1:
            p1 += 1
        elif arr[p1] == 0 and arr[p2] == 0:
            p1 += 1
            p2 -= 1
    return flags 

        
        
    # while first == -1:
    #     for i in range(len(arr)):
           
    #         if arr[i] == 1:
                
    #             first = i
    #             break
    
    # newM = [0 for _ in range(len(A))]
    # newM[first] = 1
    
    
    # #set flags back on mountain
    # for i in range(first + 1, len(arr)):
    #     no = i-peaks+1
        
    #     # print('no arr', arr[no: i])
    #     # print('i', i)
    #     if arr[i] == 1 and i > no and sum(arr[no: i]) == 0:
    #         print('put flag')
    #         print('newM i', i)
    #         newM[i] = 1
    #         print(newM)
    #     elif arr[i] == 1 and sum(arr[no: i]) > 0:
    #         arr[i] = 0
           

    # return sum(newM)
A = [1, 5]
print(peak1(A))

# arr = [0 for _ in range(len(A))]

#     for i in range(1, len(A)):
#         if A[i] > A[i-1] and A[i] > A[i+1]:
#             arr[i] = 1
#     peaks = sum(arr)
#     #print(peaks)
#     # spread = [0 for _ in range(len(arr))]
#     # apart = 0
#     perfect = 0
#     while perfect == 0:
#         peaks = sum(arr)
#         print('arr', arr, 'peaks', peaks)
#         for i in range(len(arr)):
#             if i == len(arr):
#                 perfect = 1
#             # print('sum',sum(arr[i: i+peaks]))
#             if arr[i] == 1 and sum(arr[i: (i+peaks - 1)]) >= 2:
#                 print('sum')
#             #set additional peak to 0
#                 undo = 0
#                 index = i+1
#                 while undo == 0:
#                     if arr[index] == 1:
#                         arr[index] = 0
#                         undo = 1
#                     else:
#                         index += 1
#                     print('undo', undo, 'arr', arr)
#             print(arr)
#         break
#     return sum(arr)