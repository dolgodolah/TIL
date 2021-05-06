from collections import deque
def check(s):
    stack=[]
    for i in range(len(s)):
        if stack:
            if (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')') or (stack[-1]=='{' and s[i]=='}'):
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    s=deque(list(s))
    for _ in range(len(s)):
        print(s)
        if check(s):
            answer+=1
        s.append(s.popleft())
        

    return answer


print(solution("}}}"))

