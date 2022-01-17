function bigSorting(arr){
    //sorting numbers
    arr.sort((a,b) => Number(b) - Number(a))
    //arr.reverse()  // dont need reverse, can switch (a-b) lowest first, (b-a) highest first
    return arr
}

let unsorted = ['6', '3142220', '1', '3', '10', '3', '5']
console.log(bigSorting(unsorted))


// missing digit
function missing(arr) {
    arr.sort(function(a,b){return a-b})
    for(let i=0; i<arr.length; i++){
        if(arr[i]+1 !== arr[i+1]) return arr[i]+1
    }
    return arr
}
arr = [3,1,0,5,2]
console.log(missing(arr))

