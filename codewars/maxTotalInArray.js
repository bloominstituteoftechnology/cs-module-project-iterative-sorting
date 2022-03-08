var maxSequence = function(arr){
    var max = 0;
    var cur = 0;
    arr.forEach(function(i){
      cur = Math.max(0, cur + i);
      max = Math.max(max, cur);
    });
    return max;
  }

  console.log(maxSequence([1,-2,4,-6,-8]))