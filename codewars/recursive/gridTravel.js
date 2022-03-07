const canSum1 = (target, arr, memo = {}) => {
  if (target === 0) {
    return true;
  }
  if (target < 0) {
    return false;
  }

  if (memo[target]) return memo[target];

  for (let i = 0; i < arr.length; i++) {
    if (canSum1(target - arr[i], arr, memo) === true) {
      // store in memo
      
      memo[target] = true;
      console.log({memo})
      return true; // early return inside for loop
    }
  }
  //store in memo
  memo[target] = false;
  return false;
};

//console.log(canSum1(7, [2, 4, 1]));
//console.log(canSum1(302, [7, 14]));

//  find difference from number and target
// if difference exists return
// if there is a number less than difference, add together, lower difference
// if difference or number less than difference exists add, and find new difference, until 0 or -1.
let found = null
const howSum = (target, arr, sum = 0, sumArr = []) => {
  
  console.log({found})
  if (sum === target) {
    if(found === null || found?.length > sumArr.length) found = sumArr;
    return sumArr;
  }
  if (arr.length === 0) return false;

  if (sum < target) {
    for (let i = 0; i < arr.length; i++) {
      let pushedArr = [...sumArr, arr[i]];
      let arrSpliced = [...arr];
      arrSpliced.splice(i, 1);
      howSum(target, arrSpliced, sum + arr[i], pushedArr);
    }
  }
  return found;
};
//console.log('how sum',howSum(10, [2, 4, 3, 7, 1, 0]));

let arrResults = null
const shortSum = (target, arr, arrSum = [], memo = {}) => {
  // console.log({ memo });
  
  if (memo[target]) {
    return memo[target];
  }
  if (target === 0) return arrSum;
  if (target < 0) return null;

  for (let num in arr) {
    const remainder = target - arr[num];
    const addArr = arrSum.length > 0 ? [...arrSum, arr[num]] : [arr[num]]

    if (shortSum(remainder, arr, addArr, memo) !== null) {
      if (arrResults === null || addArr.length < arrResults.length) {
       
        arrResults = shortSum(remainder, arr, addArr);
      } 
    }
  }

  return arrResults ? arrResults : null;
};
//console.log(shortSum(7, [5, 1, 2, 3, 1]));
//console.log(shortSum(8, [2, 3, 5, 9, 4]));
// console.log(shortSum(8, [1, 5, 4]));
// console.log(shortSum(8, [2, 3, 5, 1]));
// console.log(shortSum(8, [1, 4, 5]));
//console.log(shortSum(100, [1, 2, 5, 25]));

const bestSum = (target, arr, memo={}) => {
  if (memo[target]) return memo[target]
  if (target === 0) return [];
  if (target < 0) return null;
  let shortest = null;
  for (let num of arr) {
    const remainder = target - num;
    const remainderSum = bestSum(remainder, arr, memo);
    if (remainderSum !== null) {
      //console.log({remainderSum})
      let result = [...remainderSum, num];
      if (shortest === null || result.length < shortest.length) {
        shortest = result;
      }
    }
  }
 // console.log({ shortest });
  memo[target] = shortest
  return shortest;
};
 console.log(bestSum(7, [5, 7, 2, 3]));
 console.log(bestSum(8, [2, 3, 5, 1]));
 console.log(bestSum(8, [5, 2, 1]));
  console.log(bestSum(100, [1, 2, 5, 25, 1,2]));
