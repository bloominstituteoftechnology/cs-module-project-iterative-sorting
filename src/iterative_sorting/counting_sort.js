function counting_sort(arr){
    //find max value
    maxValue = Math.max(...arr)
    console.log(maxValue)
    //make arr of zeros
    zeros = new Array(maxValue + 1).fill(0)
    for (let x in arr){
        zeros[arr[x]] += 1
    }
    sorted = []
    idx = 0
    while (idx < zeros.length){
        while(zeros[idx] > 0){
            sorted.push(idx)
            zeros[idx] -= 1
        }
        idx++
    }
    return sorted
}

arr1 = [1, 1, 19, 2,5,4]
console.log(counting_sort(arr1))