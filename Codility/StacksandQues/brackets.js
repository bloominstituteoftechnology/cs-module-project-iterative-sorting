function brackets(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  if(S.length%2 !== 0) return 0
  let one = /()/gi
  let two = /[]/gi
  let three = /{}/gi
while (S.includes('()') || S.includes('[]') || S.includes('{}')) {
S=S.replace('()', '');
S=S.replace(/[]/gi, '');
S=S.replace(/{}/gi, '');
console.log({S})
return
}

if (S.length === 0) return 1;
if (S.length > 0) return 0;
}
console.log(brackets('(){[]{'));
