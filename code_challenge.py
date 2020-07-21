# Print out all of the numbers in the following array that are divisible by 3:
x = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42

def db3(x):
    for i in x:
        if i % 3 == 0:
           print(i) 
   
    

db3(x)


