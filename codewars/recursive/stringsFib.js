const makeWord = (find, arr, memo = {}) => {
  console.log({ find });
  if (memo[find]) return memo[find];
  if (find === '') return true;

  for (let word of arr) {
    let arrWord = word.split('');
    // if matches initial characters
    let findArr = find.slice(0, arrWord.length).split('');
    // if(target.indexOf(word) === 0)
    if (JSON.stringify(arrWord) === JSON.stringify(findArr)) {
      const remain = find.replace(word, '');
      console.log({ remain });
      if (makeWord(remain, arr, memo)) {
        memo[remain] = true; // store before return
        return true; // early return
      }
    }
  }
  return false;
};

//console.log(makeWord('abcdefabcdecede', ['ab', 'ce', 'de', 'f', 'a', 'abc']));

const numWays = (target, arr, memo = {}) => {
  console.log({ memo });
  if (memo[target]) return memo[target];
  if (target === '') {
    return 1;
  }
  let count = 0; // is count reseting?
  for (let word of arr) {
    if (target.indexOf(word) === 0) {
      let remain = target.replace(word, '');
      if (numWays(remain, arr, memo) === 1) {
        memo[target] = 1;
        count = count + 1;
      }
    }
  }
  return count;
};
//console.log(numWays('abcdef', ['ab', 'cde', 'de', 'f', 'a', 'abc', 'abcde']));

const typesOfWays = (target, arr) => {
  console.log('innnnn');
  if (target === '') {
    return [[]];
  }
  let final = [];
  for (let word of arr) {
    if (target.indexOf(word) === 0) {
      let remain = target.replace(word, '');
      // let remainArr = [...found, word];
      let arrCom = typesOfWays(remain, arr);

      if (arrCom) {
        const wordArr = arrCom.map((way) => [word, ...way]);
        console.log({ wordArr });
        final.push(...wordArr);
      }
    }
  }
  return final;
};

// console.log(
//   typesOfWays('abcdef', ['ab', 'cde', 'de', 'f', 'a', 'abc', 'abcde'])
// );

const allConstruct = (target, wordBank) => {
  if (target === '') return [[]];

  const result = [];

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      const remain = target.replace(word, '');
      const waysToBuildRemain = allConstruct(remain, wordBank); // return all remains
      // when we get valid data from waysToBuildRemain
      const targetWays = waysToBuildRemain.map((way) => [word, ...way]);
      result.push(...targetWays);
    }
  }
  return result;
};

console.log(allConstruct('abcdef', ['ab', 'cde', 'de', 'f', 'a', 'abc', 'abcde']));

const wordArr = (find, arr) => {
  if (find === '') return [];

  for (let word of arr) {
    // find length
    let arrWord = word.split('');
    // if matches initial characters
    let findArr = find.slice(0, arrWord.length).split('');
    if (JSON.stringify(arrWord) === JSON.stringify(findArr)) {
      console.log({ arrWord, findArr });
      const remain = find.replace(word, '');
      const found = wordArr(remain, arr);
      if (found !== null) {
        console.log({ found });
        return true;
      }
    }
  }
  return false;
};

// console.log('worrd',wordArr('abcdef', ['ab', 'ce', 'de', 'a', 'abc']));
