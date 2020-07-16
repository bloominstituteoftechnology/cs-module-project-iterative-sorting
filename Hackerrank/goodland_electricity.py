def pylons(k, arr):
    plants = -1
    #see if feasible
    for i in range(len(arr)):
        if arr[i] != 1 and i+1 < len(arr):
            possible = 0
            pt = i+1
            dist = 1
            while dist < k[-1] and pt <= len(arr):
                print('pt', pt)
                dist += 1
                #pt += 1
                print('pt', pt)
                #print('arr pt', arr[pt])

                if pt < len(arr):
                    if arr[pt] == 1:
                        possible = 1
                        break 
                else:
                    dist += 1
                    pt += 1
            print('possi', possible)
            if possible == 0:
                return -1
    
    print('ok')



k = [6,2]
arr = [0,1,1,1,1,0]
print(pylons(k, arr))