const factorial = (num) => {
  if (num <= 1) return 1;
  return num * factorial(num - 1);
};

console.log(factorial(9));

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

console.log(findadd(6));
// 3 +
// 2 + 1 = 3
// 5 + 1 = 3
// 3 + 2 = 5
// 1 + 1 = 2

// how many ways can the frog cross the river.
// river 11 feet.  10 stones to jump.
// how many ways can the frog cross the river
// can either jump one or two stones.
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

console.log(frog(4));
