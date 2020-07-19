function count_shifts(arr){
    count = 0
    for (let i=0; i< arr.length; i++){
        if (arr[i+1] < arr[i]){
            while (i >= 0 && arr[i+1] < arr[i]){
            [arr[i], arr[i+1]] = [arr[i+1], arr[i]]
            console.log('arr',arr)
            i -= 1
            count += 1
            }
        }
    }
    return count



}
arr = [2, 1, 3, 1, 1]
console.log(count_shifts(arr))