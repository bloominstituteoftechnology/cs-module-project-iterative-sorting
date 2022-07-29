
function min_max(A){
    // set max and min sum values
    let max = 0
    let min = 0
    const sorted = A.sort()
    for(let i=0; i< A.length-1; i++){
        min += A[i] 
    }
    for(let i=1; i< A.length; i++){
        max += A[i] 
    }
    return `${min} ${max}`
}



A = [7, 69, 2 ,221 ,8974]
console.log(min_max(A))