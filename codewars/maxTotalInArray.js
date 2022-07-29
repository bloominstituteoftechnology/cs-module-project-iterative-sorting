var maxSequence = function(arr){
    var max = 0;
    var cur = 0;
    arr.forEach((i) => {
      cur = Math.max(0, cur + i); // if cur is less than 0, restart at 0
      max = Math.max(max, cur);
    });
    return max;
  }

  console.log(maxSequence([1,-2,4,-6,-8]))

