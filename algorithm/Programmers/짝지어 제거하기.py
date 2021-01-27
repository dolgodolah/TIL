def solution(s):
    answer = 0
    stack = []
    idx=0
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    
    if stack:answer=0
    else:answer=1
        

    return answer

print(solution('baabaa'))
print(solution('cdcd'))