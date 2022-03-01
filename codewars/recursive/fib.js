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

console.log(fib(6))