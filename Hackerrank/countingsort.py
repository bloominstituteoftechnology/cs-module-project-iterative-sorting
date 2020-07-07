#hackerrank problem, just return array of 0s, +1 for each index
def countingSort(arr):
    #find max value
   # a value of n was provided
    countArray = [0 for _ in range(0, n)]

    for x in arr:
        countArray [x] += 1
    
    return countArray

# lambda problem, return actual array
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr

    if maximum == None:
        #set maximum to max value in array
        maximum = max(arr)

    #make a bunch of buckets 
    # make a bucket to hold each possible value
    #will create 0s, _ means not using i
    #takes max number + 1 and creates buckets for each number.
    #maximum = 19, will create 20 buckets
    # maximum + 1, because first bucket will be 0
    buckets = [0 for _ in range(maximum+1)]
    

    # buckets are now in an array of 0s,
    # if the number is in the array it will add a 1 to that index in the array
    # example if [2,2,2,20]  will be 21 buckets , and bucket[2] = 3
    for x in arr:
        if x < 0:
            return 'Error, negative numbers not allowed'
        buckets [x] += 1
    
    #we have a count for each bucket
    #Ex. use case, how many sessions on this date
    # will write array values out in order, will be sorted
    j = 0
    for i in range(len(buckets)):
        #while value of the bucket is > o
        #print that index, index is already equal to value
        # only looks for buckets > 0
        while buckets[i] > 0:
            arr[j] = i
            # j tracks index of array
            j += 1
            buckets[i] -= 1
    print(arr)
    return arr


arr1 = [1, 1, 19, 2,5,4]
print(counting_sort(arr1))