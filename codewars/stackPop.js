function validParentheses(parens) {
    if(parens.length === 0 ) return true
    if(parens.length === 1) return false
    if(parens.length % 2 != 0) return false
    let parensArr = parens.split('')
    let stack = []
    const obj = {'(':')'}
    for(let i=0; i<parensArr.length; i++){
        console.log({stack}, parensArr[i])
      if(stack.length === 0) {
        stack.push(parensArr[i])
      }else if(obj[stack[stack.length-1]] === parensArr[i]){
        stack.pop()
      } else {
        stack.push(parensArr[i])
      }
    }
    console.log('final', {stack})
    if(stack.length > 0) return false
    return true;
  }

  console.log(validParentheses("())("))