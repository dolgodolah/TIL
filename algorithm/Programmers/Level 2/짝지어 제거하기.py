# 21년 5월 5일 두번째 풀이
def solution(s):
    answer = 0
    stack=list()
    s=list(s)
    for ss in s:
        stack.append(ss)
        while len(stack)>1 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
    # print(stack)
    if not stack:
        answer=1
    return answer


# 21년 1월 27일 첫번째 풀이
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