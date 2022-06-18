function rotate(A, K) {
  rotated = new Array(A.length).fill(0); // empty arr of zeros

  while (K > 0) {
    for (let i = 0; i < A.length; i++) {
      if (i < A.length - 1) {
        rotated[i + 1] = A[i];
      } else {
        rotated[0] = A[i];
      }
    }
    K -= 1;
    A = [...rotated];
  }
  return rotated;
}
A = [9, 3, 4, 2, 4, 90, 89];
K = 14;
//console.log(rotate(A,K))

const shiftArr = (A, K) => { // 100%
  if (A.length < 2) return A;
  if (K === 0) return A;

  if (K > A.length) {
    K = K % A.length;
  }
  let shifted = [];
  for (let i = 0; i < A.length; i++) {
    if (K + (i + 1) <= A.length) {
      shifted[i + K] = A[i];
    } else {
      shifted[i + K - A.length] = A[i];
    }
  }
  return shifted;
};

//console.log(shiftArr(A,K))



