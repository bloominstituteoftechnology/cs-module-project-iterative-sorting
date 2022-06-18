function diffMin(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  // start in middle
  if (A.length === 2) return Math.abs(A[0] - A[1]);

  let sideL = A[0];
  let sideR = 0;

  for (let i = 1; i < A.length; i++) {
    sideR = sideR + A[i];
  }

  let diff = Math.abs(sideR - sideL);
  let lowest = diff;

  for (let i = 1; i < A.length; i++) {
    sideL = sideL + A[i];
    sideR = sideR - A[i];
    diff = Math.abs(sideR - sideL);
    if (diff < lowest) {
      lowest = diff;
    }
  }
  return lowest;
}

console.log(diffMin([-20, 1, 4, 11, -17, 2, 9]));


const frog2 = (X, A) => {
    if(A.length < X + 1) return -1
    if(A.length === 1 && A[0] === 1) return A[0]
    let zeros = new Array(X + 1).fill(0) // positions of 
    let max = 0
    for(let i=0; i<A.length; i++){
        let pos = A[i]
        let time = i
        if(zeros[pos] === 0){
            // console.log({pos, time})
            if(time === 0) time = 1 // want to check for zeros after running loop
            zeros[pos] = time
            // console.log({zeros})
            if (time > max) max = time
        }
    }
    zeros[0] = 1
    if(zeros.includes(0) ) return -1
    return max
}

console.log(frog2(5, [1, 3, 1, 4, 2, 3, 5, 4]))