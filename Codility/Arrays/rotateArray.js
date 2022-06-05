function rotate(A, K){
    //rotate once until K = 0
    //make empty array of zeros
    //mv = Math.max(...A)
    //console.log(mv)
    rotated = new Array(A.length).fill(0) // empty arr of zeros
   
    while(K > 0){
        console.log('A top',A)
        for(let i=0; i< A.length; i++){
            if (i < (A.length - 1)){
                rotated[i+1] = A[i]
                console.log('rotated loop', rotated)
            } else {
                rotated[0] = A[i]
            }
        }
        console.log('rotated',rotated)
        K -= 1
        A = [...rotated]
        console.log('A',A)
    }
    return rotated
}
A = [9,3,4,2,4, 90, 89]
K = 4
console.log(rotate(A,K))