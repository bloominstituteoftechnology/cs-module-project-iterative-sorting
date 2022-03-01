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
      return true;
    }
  }
  console.log({ memo });
  //store in memo
  memo[target] = false;
  return false;
};

//console.log(canSum1(7, [2, 4]));
//console.log(canSum1(302, [7, 14]));

//  find difference from number and target
// if difference exists return
// if there is a number less than difference, add together, lower difference
// if difference or number less than difference exists add, and find new difference, until 0 or -1.
let found
const howSum = (target, arr, sum = 0, sumArr = []) => {
  console.log({ target, arr, sum, sumArr });
  if(target === 0) found = []
  if (sum === target) {
    found = sumArr
    return sumArr;
  }
  if (arr.length === 0) return false;
   
  if (sum < target) {
    for (let i = 0; i < arr.length; i++) {
      let pushedArr = [...sumArr, arr[i]];
      let arrSpliced = [...arr];
      arrSpliced.splice(i, 1);
      // console.log({arrSpliced})
    howSum(target, arrSpliced, sum + arr[i], pushedArr)
    }
  }
  return found;
};
console.log(howSum(10, [2, 4, 3, 7]));
