# Task Description
# A vending machine has the following denominations: 1c, 5c, 10c, 25c, 50c, and $1. Your task is to write a program that will be used in a vending machine to return change. Assume that the vending machine will always want to return the least number of coins or notes. Devise a function getChange(M, P) where M is how much money was inserted into the machine and P the price of the item selected, that returns an array of integers representing the number of each denomination to return. 

# Example:
# getChange(5, 0.99) // should return [1,0,0,0,0,4]

def getChange(M, P):
    sep = str(P).split('.')
    print(sep)
    change = [0,0,0,0,0,0]
    paid = int(sep[1])
    #need to convert M 
    diff = M - paid

    print(diff)
    arr = []
    
    
    # if len(arr) > 0:
    #     change[5] = arr[0]
    #     remain = arr[1:] 
    #     while remain > 0:
    #         if remain > 50:
    #             change[4] += 1
    #             remain += remain - 50
    #         if remain > 25:
    #             change[3] += 1
    #             remain += remain - 25
    #         if remain > 10:
    #             change[2] += 1
    #         if remain > 5:
    #             change[1] += 1
    #         if remain[0] > 1:
    #             change[0] += 1
    #     return change


print(getChange(5, .99))