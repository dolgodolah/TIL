# 문제 잘 읽자.
def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        for i in s:
            if not i in ['0','1','2','3','4','5','6','7','8','9']:
                answer=False
                break
    else:
        answer=False
    return answer

print(solution('1111115a11'))