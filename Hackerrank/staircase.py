#print a staircase for N
def stair(N):
    #print whitespace or #
    #top stair has only 1 #, and N-1 ''
    # print multiple of something
    for i in range(N):
        print(' ' * (N-(i+1)) + '#' * (i+1) )



N = 6
print(stair(N))