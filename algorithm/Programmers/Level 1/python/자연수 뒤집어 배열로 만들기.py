def solution(n):
    answer = []
    n = reversed(str(n))
    for i in n:
        answer.append(int(i))
    return answer

print(solution(12345))