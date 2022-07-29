# A string S consisting of N characters is called properly nested if:

# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.

# Write a function:

# class Solution { public int solution(String S); }

# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".

def nested(S):
    if S == "":
        return 1
    sList = list(S)
    if len(sList)  == 2 and sList[0] == "(" and sList[-1] == ")":
        return 1
    if len(sList)  == 2 and sList[0] == ")" or sList[-1] == "(":
        return 0
    if sList[0] == "(" and sList[-1] == ")":
        answer = 1
    else: 
        return 0
    if sList.count('(') != sList.count(')'): 
        return 0
    if len(sList) > 2 and sList[0] == "(" and sList[1] == ")" and sList[2] == ")":
        return 0
    return answer

#S = "())"
#print(nested(S))


def nested2(S):
    if S == "":
        return 1
    sl = list(S)
    #remove odd number list
    if len(sl)%2 != 0:
        return 0
    print(sl)
    stack = []
    check = [')', '}', ']']
    for i in range(len(sl)):
        print('i',i)
        if sl[i] in check and len(stack) == 0:
            return 0
        if sl[i] not in check:
            stack.append(sl[i])
            print(stack)
        elif sl[i] == check[0] and stack[-1] == '(':
            stack.pop()
            print('stack', stack)
        elif sl[i] == check[0] and stack[-1] != '(':
            return 0
        elif sl[i] == check[1] and stack[-1] == '{': 
            stack.pop()
            print('stack', stack)
        elif sl[i] == check[1] and stack[-1] != '{':
            return 0
        elif sl[i] == check[2] and stack[-1] == '[':
            stack.pop()
        elif sl[i] == check[2] and stack[-1] != '[':
            return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
         
            



S = "{{{{"
# print(nested2(S))


def nested3(S):
    if S == "":
        return 1
    sl = list(S)
    #remove odd number list
    if len(sl)%2 != 0:
        return 0
    print(sl)
    stack = []
    for i in range(len(sl)):
    # check = [')', '}', ']']
    # for i in range(len(sl)):
    #     print('i',i)
    #     if sl[i] in check and len(stack) == 0:
    #         return 0
    #     if sl[i] not in check:
    #         stack.append(sl[i])
    #         print(stack)
    #     elif sl[i] == check[0] and stack[-1] == '(':
    #         stack.pop()
    #         print('stack', stack)
    #     elif sl[i] == check[0] and stack[-1] != '(':
    #         return 0
    #     elif sl[i] == check[1] and stack[-1] == '{': 
    #         stack.pop()
    #         print('stack', stack)
    #     elif sl[i] == check[1] and stack[-1] != '{':
    #         return 0
    #     elif sl[i] == check[2] and stack[-1] == '[':
    #         stack.pop()
    #     elif sl[i] == check[2] and stack[-1] != '[':
    #         return 0
    # if len(stack) == 0:
    #     return 1
    # else:
    #     return 0
         
            



S = "{{{{"
print(nested3(S))