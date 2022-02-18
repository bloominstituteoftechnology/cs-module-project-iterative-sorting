const fib = (n, memo = {}) => {
    if(memo[n]) return memo[n]
    // base case
    if(n <= 2) return 1
    // recursion
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    console.log({memo})
    return memo[n]
    
}

console.log(fib(6))