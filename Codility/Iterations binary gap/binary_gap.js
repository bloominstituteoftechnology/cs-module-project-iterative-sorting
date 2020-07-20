function binary_gap(N){
    gap = 0
    binaryNum = N.toString(2)
    console.log(binaryNum)
    count = 0
    gap = 0
    for (let c of binaryNum){
        if (c === '0'){
            count += 1
        } else if(c === '1'){
            if (count > gap){
                gap = count
            }
            count = 0
        }
    }
    return gap

}

console.log(binary_gap(35748))