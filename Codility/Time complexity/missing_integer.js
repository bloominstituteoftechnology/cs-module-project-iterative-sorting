function missing(A){ // 100% codility
    //sort
    const sortNums = (a, b) => {
        if(a > b) return 1
        if (a < b) return -1
        if (a === b) return 0
    }
    A.sort(sortNums)

    if(!A.includes(1)) return 1
    missing = A.length + 1 // last value
    for(let i=0; i<A.length; i++){
        if ((A[i]+1) != (A[i+1])){
            return A[i]+1
        } 
    }
    return missing
}
A = [2,33,12,5]
console.log(missing(A))