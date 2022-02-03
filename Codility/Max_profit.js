const profit = (A) => {
    let greater = 0
    let start
    let add = 0
    let maxProfit = 0
    for(let i=0; i<A.length; i++){
        if(A[i] < A[i+1]) greater += 1
       // starting point, profit undefined and diff pos
       // keep track of maxProfit, and if goes below starting point, switch to new start, but must beat max profit
       if(A[i+1] > A[i] && !start){
           start = i
           let sum = (A[i+1] - A[i])
           add = add + sum
           console.log({add})
           if(add > maxProfit) maxProfit = add
       } else if(A[i+1] >= A[i]  && start){
           add += A[i+1] - A[i]
           if(add > maxProfit) maxProfit = add
           console.log({maxProfit})
       } else if(A[i+1] < A[i]){
           if(A[start] > A[i]) {
               console.log('in a start > ai')
               start === i
               add === i
           } else if(start){
            add += A[i+1] - A[i]
           }
       }
    }
    if (greater === 0) return 0
    return maxProfit
}

A = [23171, 21011, 21123, 21366, 21013 ,21367, 21000, 19000]
console.log(profit(A))