function bigSorting(arr){
    //sorting numbers
    arr.sort((a,b) => Number(a) - Number(b))
    arr.reverse()
    return arr
}


let unsorted = ['6', '3142220', '1', '3', '10', '3', '5']
console.log(bigSorting(unsorted))