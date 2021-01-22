def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    answer = int(''.join(answer))
    return answer

