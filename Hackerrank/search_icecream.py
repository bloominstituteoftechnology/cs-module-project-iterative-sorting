def icecreamParlor(m, arr):
    pair = []
    for i in range(len(arr)):
        if arr[i] < (m-1):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == m:
                    pair.append(i+1)
                    pair.append(j+1)
                    return pair