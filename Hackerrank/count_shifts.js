function count_shifts(arr) {
  count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i + 1] < arr[i]) {
      while (i >= 0 && arr[i + 1] < arr[i]) {
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        console.log('arr', arr);
        i -= 1;
        count += 1;
      }
    }
  }
  return count;
}
arr = [2, 1, 3, 1, 1];
console.log(count_shifts(arr));
count = 0
function swap_order(arr) {
  if (arr.length === 1) return arr;
  let i = 0;
  while (i <= arr.length) {
    // while next item is greater than previous swap
    if (arr[i] > arr[i + 1]) {
      while (i >= 0 && arr[i] > arr[i + 1]) {
        // swap
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        i -= 1
        count += 1
      }
    } else {
      i += 1;
    }
  }
  return count;
}

arr = [2, 1, 3, 1, 1];
console.log(swap_order(arr));
