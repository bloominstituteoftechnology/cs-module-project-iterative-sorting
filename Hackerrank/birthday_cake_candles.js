function candles(A){
    //sort array
    A.sort()
    console.log(A)
    // reverse iterate
    //count
    count = 1
    pt = 2
    console.log(A[A.length - pt], A[A.length -1])
    while (A[A.length - pt] === A[A.length - 1]){
       console.log('in count', count)
        count += 1
        pt += 1
    }
    console.log({count})
    return count
}

A = [3,2,3,1,3]
console.log(candles(A))