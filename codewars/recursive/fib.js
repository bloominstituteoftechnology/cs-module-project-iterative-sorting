const fib = (n, memo = {}) => {
    if(memo[n]) {
        console.log(111, n)
        return memo[n]
    }
    // base case
    if(n <= 2){
        console.log(222, n)
        return 1
    } 
    // recursion
    console.log({n})
    memo[n] = fib(n-1, memo) + fib(n-2, memo) // stores in memo
    console.log({memo})
    
    return memo[n] // give result looking for
    
}

//console.log(fib(6))

const fibZero = (n) =>{
    let arr = new Array(n + 1).fill(0)
    arr[1] = 1
   
    for(let i=0; i<arr.length - 1; i++){
        if(i < arr.length - 2){
            arr[i+1] = arr[i+1] + arr[i]
            arr[i+2] = arr[i+2] + arr[i]
        } else {
            arr[i+1] = arr[i+1] + arr[i]
        }
    }
    console.log({arr}, arr.length)
    return arr[arr.length - 1]
}

console.log(fibZero(6))