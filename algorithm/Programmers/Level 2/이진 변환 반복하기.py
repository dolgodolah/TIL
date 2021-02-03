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
