// indexOf
   // can return first occurance in a string 
   const exString = 'eat all day day ady eat day'
   const result = exString.indexOf('all')
   console.log({result})  // 4

   // find first occurance starting at position 
   const result2 = exString.indexOf("day", 13)
   console.log({result2})

   // value not found, returns -1

// splice  
    // adds or removes an element
      // fruits.splice(position to add/ remove, how many to remove, items to add)
    const fruits = ["Banana", "Orange", "Apple", "Mango"];
    // add, acai after orange
    fruits.splice(2, 0 , 'acai')
    console.log({fruits})

    // remove banana
    fruits.splice(0, 1)
    console.log({fruits})

// slice
   // returns part of original string
   // .slice(starting, optional: ending)
   const example = 'E ai cara, fala garota  AA RR'
   const show = example.slice(5, 10)
   console.log({show})


// replace
    // replace first occurance
    const under = example.replace(' ', '_')
    console.log({under})
    // replace all, case sensitive
    const under2 = example.replace(/a/g, '_')
    console.log({under2})
    // replace all, case insensitive
    const under3 = example.replace(/r/gi, 'P')
    console.log({under3})

    function maskify(cc) {
        let last4 = cc.slice(-4) // get only last 4 digits
        let first = cc.slice(0, -4).replace(/[^0-9]/g, '#') // get all digits but last 4
        let hash = first.replace(/./g, '#')  // use . to replace any digit
        return hash + last4
     }

// Number
    let strNum = '909'
    let numNow = Number(strNum)
    console.log(typeof numNow)
    

// String
    let nowStr = String(numNow)
    //console.log({nowStr})

// String to array
// split 
// splits a string into an array of substrings.
// returns the new array.
// does not change the original string
    let eat = 'food eat all day'
    const spreadArr = [...eat]
    console.log({spreadArr})
    const splitArr = eat.split(' ')
    console.log({splitArr})

// Array to string
    const strJoin = splitArr.join()
    console.log({strJoin})
    const strJoin2 = splitArr.join('-')
    console.log({strJoin2})
    const strJoin3 = splitArr.join(' ')
    console.log({strJoin3})

// rounding : Math.floor, Math.ceil, .toFixed()

        function getMiddle(s)
        {
        console.log(s)
        //if only two, return s
        if(s.length < 3){
            return s
        }
        // if odd, return s.length/2 floor
        if(s.length % 2 !== 0){
            let middle = s.length / 2 
        middle = Math.floor(middle)
            return s[middle]
        }
        // if even, return s.length/2 , and s.length/2 + 1
        if(s.length % 2 === 0){
            let midd = s.length / 2
            console.log(s[midd], s[midd+1])
            return s[midd - 1] + s[midd]
        }
        }
    // math ceiling
    let float = 4.35
    let fixed = float.toFixed(1) //makes a string
    console.log({fixed})
    float = Math.ceil(float)
    console.log({float})

  // compare objects or arrays
  //  JSON.stringify() then compare

  // objects cannot be defined with a zero value example obj = {quarter : 0} will not define

    