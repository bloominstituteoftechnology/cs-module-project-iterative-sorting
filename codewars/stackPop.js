// function validParentheses(parens) {
//     if(parens.length === 0 ) return true
//     if(parens.length === 1) return false
//     if(parens.length % 2 != 0) return false
//     let parensArr = parens.split('')
//     let stack = []
//     const obj = {'(':')'}
//     for(let i=0; i<parensArr.length; i++){
//       if(stack.length === 0) {
//         stack.push(parensArr[i])
//       }else if(obj[stack[stack.length-1]] === parensArr[i]){
//         stack.pop()
//       } else {
//         stack.push(parensArr[i])
//       }
//     }
//     if(stack.length > 0) return false
//     return true;
//   }


//   //console.log(validParentheses("())("))

//   function removeParentheses(parens){
//     while(parens.indexOf('()') != -1){
//         parens = parens.replace('()', '');
//         console.log({parens})
//       }
//       return !parens.length;
//   }
//  // console.log(removeParentheses("()())((()))"))

// const correct = (str) => {
//   while(str.includes('()') || str.includes('{}') || str.includes('[]')){
//     str = str.replace('()', '')
//     str = str.replace('{}', '')
//     str = str.replace('[]', '')
   
//   }
//   console.log({str},  str.includes('{}'))
//   return !str.length
// }
// console.log('correct',correct("{()}[{}]"))

function getUniqueCharacter(s) {
  // Write your code here
  console.log(s.length)
  for(let i=0; i<s.length; i++){
       console.log(s.indexOf(s[i], i+1))
      if(s.indexOf(s[i], i+1) === -1){
          return i
      }
  }
}

function getUniqueCharacter1(s) {
  // Write your code here
  console.log(s.length)
  let arr = s.split('')
  let obj = {}
  for(let i=0; i<arr.length; i++){
     if(!obj[arr[i]]){
       obj[arr[i]] = 1
     } else {
       obj[arr[i]] = obj[arr[i]] + 1
     }
  }
  let result = Object.entries(obj)
  for(let i=0; i<result.length; i++){
    if(result[i][1] === 1){
      return i + 1
    }
  }
  console.log({result})
}

console.log(getUniqueCharacter1('hackthegame'))

function fourthBit(number) {
  // Write your code here
let bin = Number(number).toString(2)
console.log(bin[bin.length - 4])

}
console.log(fourthBit(23))