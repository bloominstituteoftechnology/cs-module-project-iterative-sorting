

def compareTriplets(a, b):
    score = [0,0]
    all_scores = a + b
    Ap = 0
    Bp = 3
    while Bp < 6:
        print('a',all_scores[Ap], 'b', all_scores[Bp])
        if all_scores[Ap] > all_scores[Bp]:
            score[0] += 1
        if all_scores[Ap] < all_scores[Bp]:
            score[1] += 1
        Ap += 1
        Bp += 1
    return  score
        
 

a=[5,3,9]
b=[3,3,11]

print(compareTriplets(a,b))