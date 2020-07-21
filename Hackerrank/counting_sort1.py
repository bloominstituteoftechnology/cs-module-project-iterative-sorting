maxValue = max(arr)
    countArray = [0 for _ in range(maxValue + 1)]

    for x in arr:
        countArray[x] += 1
    return countArray

#countsort 2
def countingSort(arr):
    maxValue = max(arr)
    countArray = [0 for _ in range(maxValue + 1)]

    for x in arr:
        countArray[x] += 1

    results = []
    for i in range(len(countArray)):
        while countArray[i] > 0:
            results.append(i)
            countArray[i] -= 1
    return results