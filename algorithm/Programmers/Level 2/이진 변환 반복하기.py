# 21년 5월 16일 두번째 풀이
def solution(s):
    answer = [0,0]
    while s!="1":
        tmp=""

        # 1. x의 모든 0을 제거합니다.
        for i in range(len(s)):
            if s[i]=="0":
                answer[1]+=1
            else:
                tmp+="1"
        s=tmp

        # 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
        s=format(len(s),"b")
        answer[0]+=1

    return answer


print(solution("110010101001"))



# 21년 1월 26일 첫번째 풀이
def solution(s):
    answer = []
    a,b=0,0
    while not s=='1':
        b+=s.count('0')
        s=s.replace('0','')
        s=bin(len(s))[2::]
        a+=1
    answer=[a,b]
    return answer


print(solution("110010101001"))
# print(solution("01110"))
# print(solution("1111111"))
