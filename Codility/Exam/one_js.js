solution(A, S){
    
    //cycle through additional elements
    p1 = 0
    //count num of times divides
    count = 0

    for(let i=0; i<length(A); i++){
        p1 = 0
        while (p1 < length(A)){
            amount=A.slice(i, p1)
            numD = length(A.slice(i, p1))
            if (amount%numD === 0){
                count += 1
            } 
        }
        p1 += 1
    }
    console.log(count)

}

S = 2
A= [2,1,3]
solution(A, S)