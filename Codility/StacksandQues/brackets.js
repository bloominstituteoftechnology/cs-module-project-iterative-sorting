function brackets(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  if (S.length % 2 !== 0) return 0;
  let one = /()/gi;
  let two = /[]/gi;
  let three = /{}/gi;
  while (S.includes('()') || S.includes('[]') || S.includes('{}')) {
    S = S.replace('()', '');
    S = S.replace(/[]/gi, '');
    S = S.replace(/{}/gi, '');
    console.log({ S });
    return;
  }

  if (S.length === 0) return 1;
  if (S.length > 0) return 0;
}
console.log(brackets('(){[]{'));

function stack(S) {
  if (S.length % 2 !== 0) return 0;

  // check for ending
  const end = [']', ')', '}'];
  let arr = [];
  for (let i = 0; i < S.length; i++) {
    if (!end.includes(S[i])) {
      arr.push(S[i]);
    } else if (S[i] === end[0] && arr[arr.length - 1] === '[') {
      arr.pop();
    } else if (S[i] === end[1] && arr[arr.length - 1] === '(') {
      arr.pop();
    } else if (S[i] === end[2] && arr[arr.length - 1] === '{') {
      arr.pop();
    } else {
      return 0;
    }
  }
  if (arr.length === 0) return 1;
  return 0;
}

function stack2(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  if(S.length === 0) return 1
  if(S.length%2 !== 0) return 0
  let start = []
  const end = [')', ']', '}']
  for(let item of S){
    console.log({item, start})
      if(end.includes(item)){
          if(item === ')' && start[start.length - 1] === '('){
              start.pop()
          } else if(item === ']' && start[start.length - 1] === '['){
              start.pop()
          } else if(item === '}' && start[start.length - 1] === '{'){
              start.pop()
          } else {
              return 0
          }
      } else {
          start.push(item)
      }
  }
  if(start.length === 0){
      return 1
  } else {
      return 0
  }
}

 //console.log(stack2('()()()'))

function fish(A, B) {
  // write your code in JavaScript (Node.js 8.9.4)
  // A size
  // B direction  0 - upstream, 1 - downstream
  if (!B.includes(1)) {
    return A.length;
  }
  if (!B.includes(0)) {
    return A.length;
  }

  if (A.length === 2) {
    if (B[0] === 0 && B[1] === 1) {
      return 2;
    }
    if (B[0] === 1 && B[1] === 0) {
      return 1;
    }
  }

  let up = [];
  let down = [];
  for (let i = 0; i < A.length; i++) {
    if (B[i] === 0 && down.length === 0) {
      up.push(A[i]);
    }
    if (B[i] === 0 && down.length > 0) {
      let curr = A[i];
      while (down.length > 0 && curr) {
        if (curr > down[down.length - 1]) {
          down.pop();
        } else {
          curr = false;
        }
      }
      if (down.length === 0) {
        up.push(A[i]);
      }
    }
    if (B[i] === 1) {
      down.push(A[i]); // last position
    }
    
  }
  return up.length + down.length
}

//console.log(fish([2, 3], [0, 0]));

function stoneWall(H) {
  // write your code in JavaScript (Node.js 8.9.4)
  let stack = []
  let rec = 0
  for(let i=0; i<H.length; i++){
      if(stack.length === 0) stack.push(H[i])
      if(stack.length > 0 && H[i] < stack[stack.length - 1]){
          while(stack.length > 0 && H[i] < stack[stack.length -1]){
              rec += 1
              stack.pop()
          }
          if(!stack.includes(H[i])) stack.push(H[i])
      }
      if(stack.length > 0 && H[i] > stack[stack.length - 1] && !stack.includes(H[i])){
          stack.push(H[i])
      }
  }
  return rec + stack.length
}

console.log(stoneWall([8, 8, 5, 7, 9, 8, 7, 4, 8]))