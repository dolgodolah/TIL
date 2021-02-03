def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer

print(solution(123))