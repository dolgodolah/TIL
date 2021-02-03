def solution(s):
    answer = ''
    if len(s)%2==0:#글자수가 짝수이면
        answer+=s[len(s)//2-1]+s[len(s)//2]
    else:#홀수이면
        answer+=s[len(s)//2]
    return answer

print(solution("qwer"))