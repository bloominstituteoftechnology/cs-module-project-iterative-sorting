// indexOf
// splice

function solution(A) {
  // push into an array and remove if it exists
  maxValue = Math.max(...A);

  // make array of zeros
  //count = new Array(maxValue+1).fill(0)

  odd = [];
  for (x in A) {
    let num = A[x];
    if (!odd.includes(num)) {
      odd.push(A[x]);
    } else {
      let index = odd.indexOf(A[x]);
      if (index > -1) {
        odd.splice(index, 1);
      }
    }
  }
  return odd[0];
}
arr = [9, 7, 3, 9, 3, 9, 7, 9];
//console.log(solution(arr));

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
    console.log({arr})
    if(arr.length <= 0) return 0
    arr.splice(0, 2);
    
  }
  return arr[0];
};
console.log('49', oddNum(arr));
