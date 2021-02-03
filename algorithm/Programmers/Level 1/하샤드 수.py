def solution(x):
    answer = True
    num = str(x)
    temp = 0
    for i in num:
        temp+=int(i)
    if x%temp!=0:
        answer=False
    
    return answer

print(solution(10))