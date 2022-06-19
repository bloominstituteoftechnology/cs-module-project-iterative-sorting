function bigSorting(arr) {
  //sorting numbers
  arr.sort((a, b) => Number(b) - Number(a));
  //arr.reverse()  // dont need reverse, can switch (a-b) lowest first, (b-a) highest first
  return arr;
}

let unsorted = ['6', '3142220', '1', '3', '10', '3', '5'];
console.log(bigSorting(unsorted));

// missing digit
function missing(arr) {
  arr.sort(function (a, b) {
    return a - b;
  });
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] + 1 !== arr[i + 1]) return arr[i] + 1;
  }
  return arr;
}
arr = [3, 1, 0, 5, 2];
console.log(missing(arr));

function missingInt(A) {
  // 100% Codility
  if (A.length === 1 && A[0] !== 1) return 1;
  if (A.length === 1 && A[0] === 1) return 2;
  function sortNum(a, b) {
    if (a > b) return 1;
    if (a < b) return -1;
    if (a === b) return 0;
  }

  A = A.sort(sortNum);
  A = [...new Set(A)];
  if (!A.includes(1)) return 1;
  console.log({ A });
  if (A[A.length - 1] < 1) return 1;

  for (let i = 0; i < A.length; i++) {
    if (A[i + 1] - A[i] !== 1 && A[i] + 1 > 0) {
      return A[i] + 1;
    }
  }
}

console.log(missingInt([1, 3, 6, 4, 1, 2]));

function genomicRange(S, P, Q) {
  // write your code in JavaScript (Node.js 8.9.4)
  const nul = { A: 1, C: 2, G: 3, T: 4 };
  let result = [];
  let pt = 0;
  while (pt < P.length) {
    let lowest = 4
    for (let i = P[pt]; i < Q[pt] + 1; i++) {
      if (nul[S[i]] < lowest) {
        lowest = nul[S[i]];
      }
    }
    pt += 1;
    result.push(lowest);
  }
  return result;
}

console.log(genomicRange('CAGCCTA', [2, 5, 0], [4, 5, 6]));
