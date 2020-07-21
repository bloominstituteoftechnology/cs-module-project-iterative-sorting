# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# class Solution { public int solution(String S); }

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

def brackets(S):
    if S == "":
        return 1
    sl = list(S)
    #remove odd number list
    if len(sl)%2 != 0:
        return 0
    #print(sl)
    stack = []
    check = [')', '}', ']']
    for i in range(len(sl)):
        #print('i',i)
        if sl[i] in check and len(stack) == 0:
            return 0
        if sl[i] not in check:
            stack.append(sl[i])
            #print(stack)
        elif sl[i] == check[0] and stack[-1] == '(':
            stack.pop()
            #print('stack', stack)
        elif sl[i] == check[0] and stack[-1] != '(':
            return 0
        elif sl[i] == check[1] and stack[-1] == '{': 
            stack.pop()
            #print('stack', stack)
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

print(brackets())