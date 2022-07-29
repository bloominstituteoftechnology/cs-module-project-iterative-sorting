function jumps(X, Y, D) {
    // write your code in JavaScript (Node.js 8.9.4)
    let dist = Y - X
    let jumps = dist / D 
    console.log({jumps})
    return Math.ceil(jumps)
}

console.log(jumps(10, 85, 30))