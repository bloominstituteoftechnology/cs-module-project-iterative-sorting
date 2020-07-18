function missing(A){
    //sort
    A.sort()
    console.log(A)
    missing = A.length + 1
    for(let i=0; i<A.length; i++){
        if ((A[i]+1) != (A[i+1])){
            return A[i]+1
        } 
    }
    return missing
}
A = [2,3,1,5]
console.log(missing(A))