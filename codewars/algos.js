// .split() : takes a string and turns it into an array
// .unshift() :  adds value to 0 element of array, opposite of .push
// .splice(p2, 0, n[i]) : set an value at a certain index in an array.  the 0 indicates, remove 0 existing values
// .join('') : from array to string

// reverse order
function descendingOrder(n) {
  console.log({ n });
  n = n.toString();
  n = n.split('');
  let arrRev = [];
  //...
  if (n.length === 1) {
    return Number(n[0]);
  }
  let count = 0;
  for (let i = 0; i < n.length; i++) {
    console.log('count', (count += 1), { arrRev });
    if (arrRev.length === 0) {
      arrRev.push(n[i]);
    } else if (arrRev.length === 1) {
      console.log('len 1');
      if (n[i] < arrRev[0]) {
        console.log('less', n[1], arrRev);
        arrRev.push(n[i]);
      } else {
        console.log('greater', n[1], arrRev);
        arrRev.unshift(n[i]);
      }
    } else if (arrRev.length > 1) {
      let p2 = 0;
      let insert = false;
      while (!insert) {
        if (p2 === arrRev.length) {
          arrRev.unshift(n[i]);
          insert = true;
        }
        if (n[i] >= arrRev[p2]) {
          console.log('before splice', arrRev);
          arrRev.splice(p2, 0, n[i]);
          console.log('after splice', arrRev);
          insert = true;
        } else {
          p2 += 1;
        }
      }
    }
  }
  console.log({ arrRev });
  let final = arrRev.join('');
  console.log({ final });
  let num = Number(final);
  console.log({ num });
  return num;
}

// or

const descendingOrder2 = (n) => {
  let nStr = n.toString();
  let nArr = nStr.split('');
  if (nArr.length === 1) {
    return n;
  }
  let sorted = nArr.sort();
  sorted = sorted.reverse();
  console.log({ sorted });
  let final = sorted.join('');
  console.log({ final });
  return Number(final);
};
// toLowerCase()
function alphabetPosition(text) {
  let key = {};
  const alpha = 'abcdefghijklmnopqrstuvwxyz';
  const alphaArr = alpha.split('');
  for (let i = 0; i < alphaArr.length; i++) {
    key[alphaArr[i]] = i + 1;
  }
  let textArr = text.split('');
  let numArr = [];
  for (let k = 0; k < textArr.length; k++) {
    if (key[textArr[k].toLowerCase()]) {
      numArr.push(key[textArr[k].toLowerCase()]);
    }
  }
  const numString = numArr.join(' ');
  return numString;
}
// return positions of letters only
alphabetPosition("The sun sets at 12 o'clock ");

// could have just done split('').sort().join('')
function anagrams(word, words) {
  console.log({ word, words });
  let wordObj = {};
  for (let i = 0; i < word.length; i++) {
    if (wordObj[word[i]]) {
      wordObj[word[i]] = wordObj[word[i]] + 1;
    } else {
      wordObj[word[i]] = 1;
    }
  }

  let final = [];
  for (let i = 0; i < words.length; i++) {
    if (words[i].length === word.length) {
      let match = {};
      for (let k = 0; k < words[i].length; k++) {
        if (match[words[i][k]]) {
          match[words[i][k]] = match[words[i][k]] + 1;
        } else {
          match[words[i][k]] = 1;
        }
      }

      console.log(
        JSON.stringify(Object.entries(match).sort()),
        JSON.stringify(Object.entries(wordObj).sort())
      );
      if (
        JSON.stringify(Object.entries(match).sort()) ===
        JSON.stringify(Object.entries(wordObj).sort())
      ) {
        final.push(words[i]);
      }
    }
  }
  console.log({ final });
  return final;
}

anagrams('abba', [
  'aabb',
  'abab',
  'abbaa',
  'abbab',
  'abbba',
  'abcd',
  'baaab',
  'baab',
  'baba',
  'babaa',
  'bbaa',
]);

// vending machine

const vending = (money, price) => {
  let obj = {};
  console.log({ obj });
  money = Number(money.replace('.', ''));
  price = Number(price.replace('.', ''));
  let diff = price - money;

  while (diff > 0) {
    if (diff >= 25) {
      if (!obj['quarter']) {
        obj['quarter'] = 1;
      } else {
        obj['quarter'] += 1;
      }
      diff -= 25;
    } else if (diff >= 10) {
      if (!obj['dimes']) {
        obj['dimes'] = 1;
      } else {
        obj['dimes'] += 1;
      }
      diff -= 10;
    } else if (diff >= 5) {
      if (!obj['nickles']) {
        obj['nickles'] = 1;
      } else {
        obj['nickles'] += 1;
      }
      diff -= 5;
    } else if (diff >= 1) {
      if (!obj['pennies']) {
        obj['pennies'] = 1;
      } else {
        obj['pennies'] += 1;
      }
      diff -= 1;
    }
  }
  console.log({ obj });
  return obj;
};

vending('.90', '200');

function dirReduc(arr) {
  // ...
  let dir = [];
  for (let i = 0; i < arr.length; i++) {
    let len = dir.length - 1;
    if (dir.length === 0) {
      dir.push(arr[i]);
    } else if (dir.length > 0) {
      if (arr[i] === 'NORTH' && dir[len] !== 'SOUTH') {
        dir.push(arr[i]);
      } else if (arr[i] === 'NORTH') {
        dir.pop();
      }
      if (arr[i] === 'SOUTH' && dir[len] !== 'NORTH') {
        dir.push(arr[i]);
      } else if (arr[i] === 'SOUTH') {
        dir.pop();
      }
      if (arr[i] === 'WEST' && dir[len] !== 'EAST') {
        dir.push(arr[i]);
      } else if (arr[i] === 'WEST') {
        dir.pop();
      }
      if (arr[i] === 'EAST' && dir[len] !== 'WEST') {
        dir.push(arr[i]);
      } else if (arr[i] === 'EAST') {
        dir.pop();
      }
    }
  }
  return dir;
}
