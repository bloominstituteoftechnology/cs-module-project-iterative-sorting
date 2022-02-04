function primeFactors(n) {
  //your code here
  const primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97,
  ];
  let pt = 0;
  let obj = {};
  let nums = [];
  let finish = 0;
  while (!primes.includes(n) && finish === 0) {
    if (n % primes[pt] === 0) {
      if (obj[primes[pt]]) {
        obj[primes[pt]] += 1;
      } else {
        obj[primes[pt]] = 1;
        nums.push(primes[pt]);
      }
      n = n / primes[pt];
      if (primes.includes(n)) {
        if (obj[n]) {
          obj[n] += 1;
        } else {
          obj[n] = 1;
          nums.push(n);
        }
      } else {
        pt = 0;
      }
    } else if (primes[pt] === 97) {
      obj[n] = 1;
      nums.push(n);
      finish = 1;
    } else {
      pt += 1;
    }
  }
  let result = '';
  for (let i = 0; i < nums.length; i++) {
    let value =
      obj[nums[i]] > 1 ? `(${nums[i]}**${obj[nums[i]]})` : `(${nums[i]})`;
    result = result + value;
  }
  return result;
}

//console.log(primeFactors(7917));

function chooseBestSum(t, k, ls) {
  // not enough cities
  if (ls.length < k) return null;
  ls = ls.sort();
  let biggest = null;
  let max = [];
  let maxSum = 0;
  let minSum = 0;
  let maxArr = [...ls];
  let overObj = {};
  maxArr = maxArr.reverse();

  for (let i = 0; i < k; i++) {
    max.push(maxArr[i]);
    maxSum = maxSum + maxArr[i];
    minSum = minSum + ls[i];
  }
  // maxSum less or equal to
  if (maxSum <= t) return maxSum;

  // everything too far
  if (minSum > t) {
    return null;
  } else {
    biggest = minSum;
  }

  let over = maxSum - t;
  // if can find and easy replacement
  if (overObj[over] && !maxArr.includes(overObj[over][1])) {
    return t;
  }

  // loop through to fine

  for (let i = 0; i < ls.length; i++) {
    let pt2 = i + 1;
    let pt3 = i + 2;
    let out = 0;
    while (out === 0 && i < ls.length - 4) {
      if (pt3 === ls.length - 1 && pt2 === ls.length - 2) out = 1;
      if (pt3 === ls.length - 1) {
        pt2 += 1;
        pt3 = pt2 + 1;
      }
      let sum3 = ls[i] + ls[pt2] + ls[pt3];
      if (sum3 <= t) {
        biggest = biggest < sum3 ? sum3 : biggest;
        console.log({biggest})
        pt3 += 1;
      } 
      if (sum3 >= t) {
        out = 1;
      }
    }
  }
  return biggest;
}

var ts = [50, 55, 56, 57, 58];
console.log(chooseBestSum(163, 3, ts));
ts = [50];
console.log(chooseBestSum(163, 3, ts));
ts = [91, 74, 73, 85, 73, 81, 87];
console.log(chooseBestSum(230, 3, ts));
ts= [ 73, 73, 74, 81, 85, 87, 91 ]

