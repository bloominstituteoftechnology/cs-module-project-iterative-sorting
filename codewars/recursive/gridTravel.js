const grid = (x, y, memo = {}) => {
  if (memo[`${x},${y}`]) {
    console.log('in ', { memo });
    return memo[`${x},${y}`];
  }
  // base case
  if (x === 1 && y === 1) return 1;
  if (x === 0 || y === 0) return 0;

  memo[`${x},${y}`] = grid(x - 1, y, memo) + grid(x, y - 1, memo);
  console.log({ memo });
  return memo[`${x},${y}`];
};

//console.log(grid(18, 18));

const canSum = (num, arr, pt1 = 0, pt2 = 1) => {
  // return false if checked all combinations
  // console.log({pt1, pt2})
  if (pt1 > arr.length - 1) {
    console.log({ pt1 });
    return false;
  }
  if (arr.includes(num)) return true;
  // sort arr
  arr = arr.sort();
  if (arr[0] > num) return false;

  // sum goes from start to finish
  let sum = 0;
  let loop = pt2 - pt1 + 1;

  for (let i = pt1; i < loop; i++) {
    sum = sum + arr[i];
  }
  console.log({ loop, pt2, pt1, sum });
  //console.log({sum})
  if (sum === num){
    return sum === num
  }

  // if sum less than num, recursion
  if (sum < num && pt2 < arr.length) {
    pt2 += 1;
    canSum(num, arr, pt1, pt2);
  } else {
    pt1 += 1;
    pt2 = pt1 + 1;
    canSum(num, arr, pt1, pt2);
  }
};

console.log(canSum(7, [2, 4, 3]));
