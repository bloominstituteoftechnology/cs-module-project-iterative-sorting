function solution(list) {
  const combine = (list, pt1) => {
    let first = pt1;
    let second = pt1;
    let move = true;

    while (move) {
      if (list[pt1] - list[pt1 + 1] === -1 || list[pt1 + 1] - list[pt1] === 1) {
        second += 1;
        pt1 += 1;
      } else {
        move = false;
      }
    }
    let res
    if(second - first > 1){
      res = `${list[first]}-${list[second]}`
    } else {
      res = `${list[first]},${list[second]}`
    }

    // combine first and second with -
    
    return { res, second };
  };
  // TODO: complete solution
  let pt1 = 0;
  let resultArr = [];
  while (pt1 < list.length) {
    console.log(list[pt1] - list[pt1 + 1], pt1);
    if (list[pt1] - list[pt1 + 1] === -1 || list[pt1] - list[pt1 + 1] === 1) {
      let { res, second } = combine(list, pt1);
      resultArr.push(res);
      pt1 = second + 1;
    } else {
      resultArr.push(list[pt1]);
      pt1 += 1;
    }
    // console.log({ resultArr });
  }
  resultArr = resultArr.join()
  return resultArr;
}

console.log(
  solution([
    -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20,
  ])
);
// "-6,-3-1,3-5,7-11,14,15,17-20"
