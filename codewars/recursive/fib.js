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

//console.log(fibZero(6))

const gridTravel = (m, n) => {
    const table = Array(m + 1).fill().map(() => Array(n + 1).fill(0))
    table [1][2] = 1
    table [2][1] = 1
    console.log({table})
    for(let i=1; i<table.length; i++){
        for(let k=1; k<table[i].length; k++){
            if(i === 1 && k >= 3) table [i][k] = table [i-1][k] + table [i][k-1]
            if(i === 2 && k >= 2) table [i][k] = table [i-1][k] + table [i][k-1]
            if (i > 2) table [i][k] = table [i-1][k] + table [i][k-1]
            
        }
    }
    return table [m][n]
}

console.log(gridTravel(18, 18))