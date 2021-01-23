def solution(x, n):
    answer = []
    temp = x
    for _ in range(n):
        answer.append(x)
        x+=temp
    return answer

print(solution(2,5))