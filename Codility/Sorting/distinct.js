function distinct(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  const dist = [...new Set(A)];
  return dist.length;
}

// console.log(distinct([2,1,1,2,3,1]))

function threeMult(A) {
  // 100% codility
  if (A.length === 3) return A[0] * A[1] * A[2];
  const numSort = (a, b) => {
    if (a > b) return -1;
    if (a < b) return 1;
    if ((a = b)) return 0;
  };
  const sorted = A.sort(numSort);
  const top3 = [sorted[0], sorted[1], sorted[2]];

  let org = 1;
  let alt = 3;
  // remove 0
  for (let i = 0; i < top3.length; i++) {
    if (top3[i] === 0) {
      org *= sorted[alt];
      alt += 1;
    } else {
      org *= top3[i];
    }
  }
  // try 2 negatives
  if (sorted[sorted.length - 2] < 0) {
    let topNeg =
      sorted[sorted.length - 1] * sorted[sorted.length - 2] * sorted[0];
    if (topNeg > org) org = topNeg;
  }

  return org;
}

// console.log(threeMult([-2, -1, 3, 2, 0]));

function triangle(A) {
  // 100% codility
  let sortArr = [...A];
  function order(a, b) {
    if (a > b) return 1;
    if (a < b) return -1;
    if (a === b) return 0;
  }
  sortArr.sort(order);

  for (let i = 0; i < sortArr.length; i++) {
    if (sortArr[i] + sortArr[i + 1] > sortArr[i + 2]) return 1;
  }
  return 0;
}

function disk(A) {
  // codility 87%
  let dir = [{ start: 0 - Math.abs(A[0]), end: 0 + Math.abs(A[0]) }];
  let count = 0;
  for (let k = 1; k < A.length; k++) {
    let start = k - Math.abs(A[k]);
    let end = k + Math.abs(A[k]);

    for (let i = 0; i < dir.length; i++) {
      if (dir[i].start < start && start <= dir[i].end) {
        count += 1;
      } else if (dir[i].start === start && end !== dir[i].end) {
        count += 1;
      } else if (start < dir[i].start && dir[i].start <= end) {
        count += 1;
      }
      if (count > 10000000) return -1;
    }
    dir.push({ start, end });
  }
  return count;
}

console.log(disk([1, 5, 2, 1, 4, 0]));
