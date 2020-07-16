function change(P, M){
    //take . off M
    change = [0,0,0,0,0,0]
    money = M.toString()
    
    money = money.replace('.', '')
    payment = P.toString()
    if (!payment.includes('.')){
        payment = payment + '00'
    }
    //put to int
    money = parseInt(money)
    payment = parseInt(payment)
    let diff = payment - money
    
    while (diff > 0){
        console.log(diff)
        if (diff >= 100){
            change[5] += 1
            diff -= 100 
            console.log(diff)
        } else if(diff >= 50){
            change[4] += 1
            diff -= 50
        }
        else if(diff >= 25){
            change[3] += 1
            diff -= 25
        }else if(diff >= 10){
            change[2] += 1
            diff -= 10
        }else if(diff >= 5){
            change[1] += 1
            diff -= 5
        }else if(diff >= 1){
            change[0] += 1
            diff -= 1
        }
    }
    return change



}

console.log(change(5, 1.99))