function comparescore(a,b){
    score = [0,0]
    pt = 0
    while (pt <= a.length){
        if (a[pt] > b[pt]){
            score[0] += 1
        } else if(b[pt] >a[pt]){
            score[1] += 1
        }
        pt += 1
    }
    return score
}


a=[5,8,9]
b=[3,3,11]

console.log(comparescore(a,b))