const factorial = (num) => {
  if (num <= 1) return 1;
  return num * factorial(num - 1);
};

//console.log(factorial(9));

// 2 * 1 = 2
// 3 * 2 = 6
// 4 * 6 = 24

// return the nth number in sequence
// first and second digits are 1, 3rd digit = f(3-1) + f(3-2)
// add previous 2 results
const findadd = (num) => {
  if (num <= 0) return 0;
  if (num <= 2) return 1;

  return findadd(num - 1) + findadd(num - 2);
};

console.log('findadd', findadd(6));

// 3 +
// 2 + 1 = 3
// 5 + 1 = 3
// 3 + 2 = 5
// 1 + 1 = 2

// how many ways can the frog cross the river.
// river 11 feet.  10 stones to jump.
// how many ways can the frog cross the river
// can either jump one or two stones.
const jump = (ft, count = 0, memo = {}) => {
  if (memo[ft]) return memo[ft];
  if (ft < 0) return null;
  if (ft === 0) count = count + 1;
  if (ft >= 1) {
    memo[ft] = jump(ft - 1, count) + jump(ft - 2, count);
    return memo[ft];
  }
  return count;
};
console.log('jump', jump(6));

let count = 0;
const frog = (feet) => {
  if (feet === 0) {
    count = count + 1;
  }

  if (feet > 0) {
    frog(feet - 1, count);
    frog(feet - 2, count);
  }
  return count;
};

console.log(frog(6));

const jump2 = (pads) => {
  if (pads === 0) return 1;
  if (pads < 0) return 0;

  return jump2(pads - 1) + jump2(pads - 2);
};
console.log('jump 2', jump2(10));

const bS = (target, count, arr = []) => {
  if (target === 0) return arr;
  if (target < 0) return null;

  for (let i = 0; i < target.length; i++) {}
};
console.log(bS(9, [4, 2, 3, 6, 1]));
const bestSum = (target, nums, arr = []) => {
  if (target === 0) return arr;
  if (target < 0) return null;
  let result = null;
  for (let num of nums) {
    let redTar = target - num;
    let redArr = [...arr, num];
    //console.log({ redTar, target, redArr });
    let done = bestSum(redTar, nums, redArr);
    if (done && done !== null) {
      //console.log({ result, done });
      if (result === null || done.length < result?.length) {
        result = done;
      }
    }
  }
  return result;
};
console.log('bestSum', bestSum(9, [4, 2, 3, 6, 1]));

const nest = (target, nums) => {
  if (target === 0) return []; // retuns an empty array, will need to put recursive results in array
  if (target < 0) return null;
  let result = null;

  for (let num of nums) {
    let redTar = target - num;
    // done ? console.log([...done]) : null
    let done = nest(redTar, nums); // will run until hits a base case, after hits base case will go to next line
    if (done !== null) {
      console.log(redTar, [...done]);
      let final = [...done, num]; // target was reduced by num, need to add num to array
      if (result === null || final.length < result?.length) {
        result = final;
      }
    }
  }
  return result;
};

console.log('nest', nest(9, [4, 2, 3, 6]));

// how many ways can hit target
const waysTarget = (tar, arr, count = 0, ind) => {
  if (tar === 0 && ind === arr.length - 1) return 1;
  if (tar != 0 && ind === arr.length - 1) return 0;

  for (let i = 0; i < arr.length; i++) {
    let addTar = tar + arr[i]
    let redTar = tar - arr[i]
    return (
      waysTarget(addTar, arr, count, i) +
      waysTarget(redTar, arr, count, i)
    );
  }
};

console.log(waysTarget(3, [1, 1, 1, 1, 1]));
