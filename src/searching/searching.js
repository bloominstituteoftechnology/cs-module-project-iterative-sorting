function linSearch(A, target) {
  for (let i = 0; i < A.length; i++) {
    if (A[i] === target) {
      return i;
    }
  }
  return -1;
}
A = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9];
target = -6;
console.log(linSearch(A, target));

function linSearch(A, target) {
  if (target > A[-1]){
      return -1
  }
  if (target < A[0]){
    return -1
}
  mid = Math.floor(A.length / 2);
  console.log(mid);
  count = 0;
  while (count < mid) {
    if (A[mid] === target) {
      return mid;
    } else if (A[mid + 1] === target) {
      return mid + 1;
    } else if (A[mid - 1] === target) {
      return mid - 1;
    } else if (target > mid){
        mid = mid + Math.floor(mid / 2)
        count += 1
    } else if (target < mid){
        mid = Math.floor(mid / 2)
        count += 1
    }
  }
  return -1
}
A = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9];
target = -10;
console.log(linSearch(A, target));
