# 문제가 구리다.
# split()을 통해 공백문자를 기준으로 분리해줬는데
# 단어를 구분하는 공백문자가 아닌 것도 있도 있어서
# split(" ")을 통해 공백문자를 분리해줘야한다. 
# "   a" 이런 문자도 있다는 소리다. 
def solution(s):
    answer = ''
    ss=s.split(" ")
    for i in ss:
        answer+=i.capitalize()+" "
    return answer[:-1]

print(solution("3people unFOLLowed me"))
print(solution("aa"))
