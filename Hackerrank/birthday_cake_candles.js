function candles(A){
    //sort array
    A.sort()
    console.log(A)
    // reverse iterate
    //count
    count = 1
    pt = 2
    console.log(A[A.length -1])
    while (A[A.length - pt] === A[A.length - 1]){
       
        count += 1
        pt += 1
    }
    return count
}

A = [3,2,3,1,3]
console.log(candles(A))