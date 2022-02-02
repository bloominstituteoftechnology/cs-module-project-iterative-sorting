function plus_minus(A){
    let plus = 0
    let minus = 0
    let zero = 0
    for(let i=0; i<A.length; i++){
        if(A[i] < 0) minus += 1
        if(A[i] === 0) zero += 1
        if(A[i] > 0){
            plus += 1
            console.log('in plus', plus)
        } 
    }
    console.log({plus, minus, zero})
    plus = plus/A.length
    minus = minus/A.length
    minus = minus.toFixed(2)
    zero = zero/A.length
    zero = zero.toFixed(2)
    return `plus ${plus}, minus ${minus}, zero ${zero}`
}

A = [-4,3,-9,0,4,1]
console.log(plus_minus(A))