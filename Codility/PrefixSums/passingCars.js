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
//console.log(passingCars());

function countDiv(A, B, K) {
  // write your code in JavaScript (Node.js 8.9.4)
  let max = Math.floor(B / K);
  let min = A % K === 0 ? A / K - 1 : Math.floor(A / K);

  return max - min;
}

function minAvg(A) {
  let unique = new Set(A);
  if (unique.length === 1) return 0;
  if (A.length === 2) return 0;

  let min = (A[0] + A[1]) / 2;
  let maxInd = A[0];
  let index = 0;

  // slice
  for (let s = 0; s < A.length - 1; s++) {
    if (A[s] <= maxInd) {
      let stop = false;
      let i = s;
      let preAvg;
      while (i < A.length && !stop) {
        let slice = A.slice(s, i + 2);
        let sum = slice.reduce(function (a, b) {
          return a + b;
        });
        let avg = sum / slice.length;
        if (avg > preAvg) stop = true;
        preAvg = avg;
        if (avg < min) {
          maxInd = A[s];
          min = avg;
          index = s;
        }
        i += 1;
      }
    }
  }
  return index;
}

const minAvg2 = (A) => {
  let unique = new Set(A);
  if (unique.length === 1) return 0;
  if (A.length === 2) return 0;
  let min = (A[0] + A[1]) / 2;
  let index = 0;
  let maxInd = A[0];

  for (let i = 0; i < A.length - 1; i++) {
    if (A[i] <= maxInd) {
      if ((A[i] + A[i + 1]) / 2 < min) {
        min = (A[i] + A[i + 1]) / 2;
        index = i;
      }
    }
  }

  for (let i = 0; i < A.length - 2; i++) {
    if (A[i] <= maxInd) {
      if ((A[i] + A[i + 1] + A[i + 2]) / 3 < min) {
        min = (A[i] + A[i + 1] + A[i + 2]) / 3;
        index = i;
      }
    }
  }
  return index;
};
console.log(minAvg2([4, 2, 2, 5, 1, 9, 8]));
