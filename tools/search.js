// search for target


const binary_search = (A, target) => {
    let mid = Math.floor(A.length / 2)
    console.log(typeof mid)
    if (A[mid] === target) return mid
    if(A[mid] > target){
        console.log('greater', mid, A[mid])
        while(A[mid] > target){
            mid -= 1
            console.log({mid})
            if(A[mid] === target){
                console.log('>',{mid})
                return mid
            }
        }
        
    }

    if(A[mid] < target){
        console.log('in less', A[mid])
        while(A[mid] < target && mid <= A.length - 1){
            console.log({mid})
            mid = mid + 1
            console.log('less', mid, A[mid])
            if(A[mid] === target){
                console.log('<',{mid})
                return mid
            }
        }
    }
}
A = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
target = 0
binary_search(A, target)