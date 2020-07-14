def solution(A):
    vacations = list(set(A))
    trips = len(vacations)

    p1 = 0
    p2 = trips
    arr = []
    for i in range(len(A)):
        p1 = i
        p2 = trips
        while p2 <= len(A):
            if vacations == list(set(A[p1:p2])):
                arr.append(p2 - p1) 
            p2 += 1
    return min(arr)





A = [7,5,2,7,2,7,4,7]
print(solution(A))