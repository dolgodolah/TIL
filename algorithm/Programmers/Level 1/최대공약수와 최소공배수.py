def solution(n, m):
    answer = []
    a,b=n,m
    if n>m:
        a,b=m,n
    while True:
        a,b=b,a%b
        if b==0:
            answer.append(a)
            break
    answer.append(n//a*m//a*a)
    return answer

print(solution(3,12))