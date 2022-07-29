def binary_gap(N):
    # '''
    # A binary gap within a positive integer N is any maximal
    # sequence of consecutive zeros that is surrounded by ones
    # at both ends in the binary representation of N.
    # Args:
    #   - 
    # ...
    #bin make binary, do not need first two characters ob
    # binary makes a string

    # binaryNum, do not need first two characters
    binaryNum = bin(N)[2:]
    print(binaryNum)
    largestgap = 0
    counter = 0
    for x in binaryNum:
        if x == '0':
            #startcount = 1
            counter += 1
        #only count as binary gap if ends with 1
        #if not zero its a 1, compare counter to largestgap and restart counter
        else:
            if counter > largestgap:
                largestgap = counter
            counter = 0
    return largestgap


           

print(binary_gap(352))