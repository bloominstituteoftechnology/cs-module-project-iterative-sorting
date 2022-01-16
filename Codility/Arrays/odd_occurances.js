// indexOf
// splice

function solution(A){
    // push into an array and remove if it exists 
    maxValue = Math.max(...A)
    
    // make array of zeros
    //count = new Array(maxValue+1).fill(0)
    
    odd = []
    for (x in A){
        let num = A[x]
        if (!odd.includes(num)){
            odd.push(A[x])
        } else {
            let index = odd.indexOf(A[x])
            if (index > -1) { odd.splice(index, 1) }
        } 
    }
    return odd[0]  
}
arr = [9,3,9,3,9,7,9]
console.log(solution(arr))