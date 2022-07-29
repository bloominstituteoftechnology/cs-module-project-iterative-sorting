function solution(A) { // 100% codility
  // write your code in JavaScript (Node.js 8.9.4)
  if (A.length === 1 && A[0] === 1) return 1;
  if (A.length === 1 && A[0] !== 1) return 0;
  let obj = {};
  let count = 0;
  let max = 0;
  for (let item of A) {
    if (item > max) max = item;
    if (!obj[String(item)]) {
      obj[item] = 1;
    } else {
        return 0
    }
    count += 1
  }
  console.log({obj, count, max})
  if (count === max) {
    return 1;
  } else {
    return 0;
  }
}

console.log(solution([2,1,1,2,4]))


function maxCounter(N, A){ // 100% codility
      // write your code in JavaScript (Node.js 8.9.4)
      let counter = new Array(N).fill(0)
      let max = 0
      let updateMax = 0
  
      for(let val of A){
          if(val <= N){
            if(counter[val - 1] < updateMax) {
                let num = counter[val - 1] = updateMax + 1
                if(num > max) max = num
            } else {
                let num = counter[val - 1] += 1
                if(num > max) max = num
            } 
          } else {
              // max
              // counter = new Array(N).fill(max)
              updateMax = max
          }
      }
      for(let i=0; i<counter.length; i++){
        if(counter[i] < updateMax){
            counter[i] = updateMax
        }
      }
      return counter
} 

console.log(maxCounter(5, [4, 4, 4, 6, 4, 4, 4, 6, 3, 6]))