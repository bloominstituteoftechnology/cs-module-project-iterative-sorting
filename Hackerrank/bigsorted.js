function bigSorting(arr){
    //sorting numbers
    arr.sort((a,b) => a-b)
    for (x in arr){
        console.log(arr[x])
    }
}


unsorted = ['6', '3142220', '1', '3', '10', '3', '5']
console.log(bigSorting(unsorted))