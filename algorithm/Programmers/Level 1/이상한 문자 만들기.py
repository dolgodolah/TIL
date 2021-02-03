#upper():소문자->대문자, 대문자->대문자
#lower():대문자->소문자, 소문자->소문자
def solution(s):
    answer = ''
    val=0
    for i in s:
        if i==" ":
            val=0
            answer+=i
            continue
        if val%2==0:
            answer+=i.upper()
        elif val%2==1:
            answer+=i.lower()
        val+=1
    return answer

print(solution("try hello world"))
