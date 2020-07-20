function bubble_sort(arr1){
    for(let i=1; i<arr1.length; i++){
        while (i > 0){
            if (arr1[i] < arr1[i-1]){
                //swap
                [arr1[i], arr1[i-1]] = [arr1[i-1], arr1[i]]
                i -= 1
            } else {
                break
            }
        }
    }
    return arr1
}


arr1 = [1, 5, 8, 4, 29, 9, 6, 0, 3, 7, 9, 67]
console.log(bubble_sort(arr1))