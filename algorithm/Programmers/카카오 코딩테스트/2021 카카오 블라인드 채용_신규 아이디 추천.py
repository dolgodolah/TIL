#문제에서 주어진 단계별로 구현 해주면 된다.

def solution(new_id):
    answer = ''
    #1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id=new_id.lower() 

    #2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    temp=''
    for i in new_id:
        if i.isdecimal() or i.isalpha() or i=='-' or i=='_' or i=='.':
            temp+=i

    #3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    temp=list(temp)
    idx=0
    while idx<len(temp):
        if idx+1<len(temp) and temp[idx]=='.' and temp[idx+1]=='.':
            temp.pop(idx)
            continue
        idx+=1

    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if temp and temp[0]=='.':temp.pop(0)
    if temp and temp[-1]=='.':temp.pop()
    
    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not temp:
        temp.append('a')

    #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(temp)>=16:
        temp=temp[0:15]
        if temp[-1]=='.':
            temp.pop()

    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(temp)<=2:
        while len(temp)<3:
            temp.append(temp[-1])
            
    answer=''.join(temp)
    return answer


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))

