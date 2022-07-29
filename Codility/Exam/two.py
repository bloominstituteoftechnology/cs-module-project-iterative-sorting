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
            print('p2',p2)
            print(A[p1:p2])
            if vacations == list(set(A[p1:p2])):
                arr.append(p2 - p1) 
            p2 += 1
    return min(arr)


A = [7,5,2,7,2,7,4,7]
#print(solution(A))


def solution1(A):
    vacations = list(set(A))
    # will be at least 4 days
    days = 4
    dayArr = []
    maxWhile = len(A) + 1
    # start with first day, capture a range of 4 days verify all vacations are fulfilled
    for i in range(0, (len(A)-days)):
        print('i', i)
        days = i+4
        pt = i + days
        print('pt',pt)
        while pt <= len(A):
            print('days', days)
            #print('pt', pt)
            print(A[i:days])
            if list(set(A[i:days])) == vacations:
                dayArr.append(days)
                break
            #move pointer and days
            else:
                days += 1
                pt += 1

            

    # if not, add additional days until fulfilled.
    # then start with next day
    





A = [7,5,2,7,2,7,4,7]
print(solution1(A))