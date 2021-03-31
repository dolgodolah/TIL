# 'A'~'Z'를 밀어서 암호화했는데 A-Z 아스키코드값을 벗어났을 때
# 예를 들어 Z를 3만큼 밀면 아스키코드값이 93이 되는데 이걸 67이 되게끔 하자
def solution(s, n):
    answer = ''
    for i in s:
        if 65<=ord(i)<=90: #A-Z
            if ord(i)+n>90:
                answer+=chr(ord(i)+n-26)
                continue
            answer+=chr(ord(i)+n)
        elif 97<=ord(i)<=122: #a-z
            if ord(i)+n>122:
                answer+=chr(ord(i)+n-26)
                continue
            answer+=chr(ord(i)+n)
        else:#공백
            answer+=i
    return answer

print(solution('a B z',4))