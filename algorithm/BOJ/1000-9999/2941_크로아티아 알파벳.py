# 처음 내 풀이는 문자열 인덱싱을 통해 접근했다. 문자열의 길이가 3일 때 text[3]은 인덱싱 에러가 뜨지만
# text[0:5]와 같이 범위를 인덱싱할 때는 에러가 뜨지 않는다.
# 인덱싱을 통해 해당 범위 안에 크로아티아 알파벳이 존재한다면 idx를 알맞게 변경해주고 answer+1을 해준다.

# 다른 풀이를 보니 replace를 통해 해결했다.
# 문자열을 입력받고 크로아티아 알파벳들마다 '@'로 대체하여 최종적으로 바뀐 문자열의 길이를 출력한다.
# replace('바꿀 문자', '바뀔 문자') 바꿀 문자가 해당 문자열에 존재하지 않아도 에러가 발생하지 않는다.


# 깔끔한 풀이
text=input()
ls=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in ls:
    text=text.replace(i,'@')
print(len(text))



# 내 풀이
text=input()
idx=0
ls=['c=','c-','dz=','d-','lj','nj','s=','z=']
answer=0
while idx<len(text):
    if text[idx:idx+3] in ls:
        idx+=3
        answer+=1
    elif text[idx:idx+2] in ls:
        idx+=2
        answer+=1
    else:
        idx+=1
        answer+=1
print(answer)
