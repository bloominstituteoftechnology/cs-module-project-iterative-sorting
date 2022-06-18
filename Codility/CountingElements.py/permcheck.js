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
