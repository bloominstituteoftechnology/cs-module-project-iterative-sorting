# A string S consisting of N characters is considered to be properly nested if any of the
#  following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "(()()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

def properly(S):
    if S == "":
        return 1
    sList = list(S)
    print(sList)
    bad_dir = [')', '}', ']']
    bad_dir2 = ['(', '{','[']
    answer = 0
    if sList[0] == "(" and sList[-1] == ")":
        answer = 1
    if sList[0] == "{" and sList[-1] == "}":
        answer = 1
    if sList[0] == "[" and sList[-1] == "]":
        answer = 1
    if sList.count('(') != sList.count(')'): 
        return 0
    if sList.count('{') != sList.count('}'): 
        return 0
    if sList.count('[') != sList.count(']'): 
        return 0
    if len(sList) > 2 and sList[0] in bad_dir or sList[-1] in bad_dir2:
        return 0
    if len(sList) > 2 and sList[0] in bad_dir2 and sList[1] in bad_dir and sList[2] in bad_dir:
        return 0
    
   
    
    return answer
    


S = "()"
print(properly(S))


# 50%
# def solution(S):
#     # write your code in Python 3.6
#     if S == "":
#         return 1
#     sList = list(S)

#     bad_dir = [')', '}', ']']
#     bad_dir2 = ['(', '{','[']
#     answer = 0
#     if sList[0] == "(" and sList[-1] == ")":
#         answer = 1
#     if sList[0] == "{" and sList[-1] == "}":
#         answer = 1
#     if sList[0] == "[" and sList[-1] == "]":
#         answer = 1
#     if sList[1] in bad_dir:
       
#         answer = 0
#     if sList[-2] in bad_dir2:
#         answer = 0
#     return answer