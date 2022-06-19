// indexOf
// splice
function odd(A) {
  // 88% codility, too slow
  // write your code in JavaScript (Node.js 8.9.4)
  let obj = {};
  if (A.length === 1) return A[0];
  for (let i = 0; i < A.length; i++) {
    if (obj[A[i]]) {
      obj[A[i]] = obj[A[i]] + 1;
    } else {
      obj[A[i]] = 1;
    }
  }
  let entriesArr = Object.entries(obj);
  for (let item of entriesArr) {
    if (item[1] % 2 !== 0) return Number(item[0]);
  }
}

// indexOf() values must me strings

// console.log(odd([2, 9, 8, 2, 9, 8, 7]));

function odd2(A) {
  // 100%
  if (A.length === 1) return Number(A[0]);
  let sorted = A.sort();
  for (let i = 0; i < A.length; i += 2) {
    if (sorted[i] !== sorted[i + 1]) return sorted[i];
  }
}
console.log(odd2([2, 9, 8, 2, 9, 8, 7]));

const findOdd = (arr) => {
  arr = arr.sort();
  let newArr = [...arr];
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] === arr[i + 1]) {
      newArr.splice(i, 2); //splice at index, 2 spaces
    }
  }
  return newArr[0];
};
//console.log('36', findOdd(arr));

const oddNum = (arr) => {
  arr = arr.sort();

  while (arr[0] === arr[1]) {
    console.log({ arr });
    if (arr.length <= 0) return 0;
    arr.splice(0, 2);
  }
  return arr[0];
};
//console.log('49', oddNum(arr));

function furyRoad(R) {
  // 100% codility
  // write your code in JavaScript (Node.js 8.9.4)
  const sc = { A: 5, S: 40 };
  const ft = { A: 20, S: 30 };

  if (!R.includes('S')) {
    return R.length * 5;
  }
  if (!R.includes('A')) {
    return R.length * 30;
  }
  let min;
  let sct = 0;
  let foot;
  let startS = false;
  let pt = 0;
  while (pt < R.length) {
    if (startS === false && R[pt] === 'S' && R[pt + 1] === 'S') startS = true;
    if (startS === false && R[pt] === 'S' && !R[pt + 1]) startS = true;

    if (startS === false) {
      sct += sc[R[pt]];
    }

    if (startS === true) {
      if (!foot) {
        foot = sct > 0 ? sct : 0;
        foot += ft[R[pt]];
      } else {
        foot += ft[R[pt]];
      }
      sct += sc[R[pt]];
    }
    if (sct < foot) foot = sct;
    pt += 1;
  }
  if (foot < sct) {
    min = foot;
  } else {
    min = sct;
  }
  return min;
}

console.log(furyRoad('SSA'));
