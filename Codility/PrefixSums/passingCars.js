function passingCars(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let arr = [];
  let count = 0;
  for (let i = 0; i < A.length; i++) {
    if (A[i] === 0) arr.push(0);
    if (A[i] === 1) {
      count += arr.length;
    }
    if (count > 1000000) return -1;
  }
  return count;
}
console.log(passingCars());

function countDiv(A, B, K) {
  // write your code in JavaScript (Node.js 8.9.4)
  let max = Math.floor(B / K);
  let min = A % K === 0 ? A / K - 1 : Math.floor(A / K);

  return max - min;
}
