#can only blow out tallest candles, how many can she blow out
def candles(ar):
    tallest = 0
    count = 0
    for x in ar:
        print(x)
        if x == tallest:
            print('== tallest')
            count += 1
        elif x > tallest:
            print('> than ')
            tallest = x
            count = 1
    return count



A = [3,2,1,3]
print(candles(A))