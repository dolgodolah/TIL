# 프로그래머스 문제는 좋은게 매번 새로운 걸 배우는 느낌이다.
# 문자열 p에 대한 처리와 주어진 조건에 맞게 재귀함수를 구현하면 된다.

def dfs(p):
    if p=='': # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        return ''

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u,v='',''
    for i in range(len(p)):
        if p[i]=='(':
            u+='('
        elif p[i]==')':
            u+=')'
        if u.count('(')==u.count(')'):
            break
    if i+1<len(p):
        v+=p[i+1::]
    # print(u,v)

    #문자열 u가 "올바른 괄호 문자열"인지 "균형잡힌 괄호 문자열"인지 확인한다.
    ls = [u[0]]
    for i in range(1,len(u)):
        if ls[-1]=='(' and u[i]==')':
            ls.pop()
        else:
            ls.append(u[i])
    if not ls: #올바른 괄호 문자열이라면
        v=dfs(v) # 3. 문자열 v에 대해 1단계부터 다시 수행합니다. 
        return u+v # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.   

    else: #올바른 괄호 문자열이 아니라면,(균형잡힌 괄호 문자열이라면)
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        # 4-3. ')'를 다시 붙입니다. 
        v='('+dfs(v)+')'

        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        temp = list(u)
        temp.pop(0)
        temp.pop()
        for i in range(len(temp)):
            if temp[i]=='(':
                temp[i]=')'
            elif temp[i]==')':
                temp[i]='('
        u=''.join(temp)
        v=v+u
        return v # 4-5. 생성된 문자열을 반환합니다.

    
    
    
def solution(p):
    answer = ''
    answer=dfs(p)
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

