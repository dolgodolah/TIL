def solution(n):
    answer =  0
    if n**(1/2)%1==0:
        answer = (n**(1/2)+1)**2
    else:
        answer = -1
    return answer


print(solution(3))
