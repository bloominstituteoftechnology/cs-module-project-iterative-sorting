// # You are given integers K, M and a non-empty array A consisting of N integers. 
// # Every element of the array is not greater than M.

// # You should divide this array into K blocks of consecutive elements. 
// # The size of the block is any integer between 0 and N.
// #  Every element of the array should belong to some block.

// # The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. 
// # The sum of empty block equals 0.

// # The large sum is the maximal sum of any block.

// # For example, you are given integers K = 3, M = 5 and array A such that:

// #   A[0] = 2
// #   A[1] = 1
// #   A[2] = 5
// #   A[3] = 1
// #   A[4] = 2
// #   A[5] = 2
// #   A[6] = 2
// # The array can be divided, for example, into the following blocks:

// # [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
// # [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
// # [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
// # [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
// # The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

// # Write a function:

// # class Solution { public int solution(int K, int M, int[] A); }

// # that, given integers K, M and a non-empty array A consisting of N integers, 
// # returns the minimal large sum.

// # For example, given K = 3, M = 5 and array A such that:

// #   A[0] = 2
// #   A[1] = 1
// #   A[2] = 5
// #   A[3] = 1
// #   A[4] = 2
// #   A[5] = 2
// #   A[6] = 2
// # the function should return 6, as explained above.

// # Write an efficient algorithm for the following assumptions:

// # N and K are integers within the range [1..100,000];
// # M is an integer within the range [0..10,000];
// # each element of array A is an integer within the range [0..M].

// function solution(K,M,A){
//     //isolate highest number and see if remaining divided blocks are less than
//     //find index of highest value
//     let maxIndex
//     for(let i=0; i<A.length;i++){
//         if (A[i] === M){
//             maxIndex = i
//         }
//     }
//     if i 

// }

// K = 3
// M = 6
// A = [5, 2, 3, 4, 6]
// console.log(solution(K, M, A))

function binary(N) {
    // write your code in JavaScript (Node.js 8.9.4)
    let bin = N.toString(2)
    // if no zero, less than two ones
    if(!bin.includes('0')){
        return 0
    } 
    // find indexs of 1
    let ind = []
    for(let i=0; i<bin.length; i++){
        if(bin[i] === '1') ind.push(i)
    }
    if(ind.length < 2){
        return 0 
    }
    // find differences 
    let max = 0
    for(let i=0; i<ind.length - 1; i++){
        let dif = ind[i+1] - ind[i]
        if(dif > max){
            max = dif
        } 
    }
    return max - 1
}

console.log(binary(1041))