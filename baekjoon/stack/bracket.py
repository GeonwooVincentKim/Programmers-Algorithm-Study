def solution(s):
    if (s[0] == ")" or s[-1] == "("):
        return False

    open, close = 0, 0

    for i in range(len(s)):
        if (s[i] == "("):
            open += 1
        elif (s[i] == ")"):
            close += 1
        
            if close > open:
                return False
    
    if open == close:
        return True
    else: 
        return False


a = int(input())

for i in range(a):
    string = input()
    if (solution(string) == False):
        print("NO")
    elif (solution(string) == True):
        print("YES")
    

    
"""
1. Check the first and last index validated
- 1. If first Index value is ')', it returns False
- 2. If last Index value is '(', it returns False

2. Get All value from string
3. If the values starting from '(', it plus 1 to `open` value
4. If the values ending as ')', it plus 1 to `close` value
"""