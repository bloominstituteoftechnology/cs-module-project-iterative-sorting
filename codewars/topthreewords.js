function topThreeWords(text) {
  //replace special characters with whitespace
  let regex = /^[a-zA-Z\']/g;

  console.log({ text });
  let textArr = text.split(' ');
  let obj = {}
  for (let i=0; i< textArr.length; i++){
      let lower = textArr[i].toLowerCase()
      lower = lower.replace(!regex, ' ')
      if(obj[lower]){
          obj[lower] = obj[lower] + 1
      } else {
        obj[lower] = 1
      }
  }
  console.log({ textArr, obj });
  const entries = Object.entries(obj)
  console.log({entries})
  let first, second , third
  for(let i=0; i<entries.length; i++){
      if(!first){
        first = entries[i][0]
      } else if(obj[entries[i][0]] >= obj[first]) {
          third = second
          second = first
          first = entries[i][0] 
      } else if(obj[entries[i][0]] >= obj[second]){
          third = second
          second = entries[i][0]
      } else if(obj[entries[i][0]] >= obj[third]){
          third = entries[i][0]
      }
  }
  return [third, second, first]
}

//topThreeWords("a a a ! b  c c  d d d d  e e e e e")

topThreeWords("CyC b b b'");
