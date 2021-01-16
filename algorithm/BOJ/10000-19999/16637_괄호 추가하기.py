# 혼자서 도저히 못풀겠어서 풀이를 매우 참고했으니 이 문제는 나중에 꼭 한번 다시 풀어보자.
# eval 기능을 처음 배웠다. text='3+5'가 있을 때 eval(text)를 하면 int형 8이 반환된다.
 
# 3개의 난관이 있었다.
# 1. 풀이 아이디어 자체가 쉽게 떠오르지 않았다.
# 2. answer의 초기값을 0으로 해놨는데 실제 정답은 2^31보다 작고 '-2^31'보다 컸다.
# 3. n이 1일 때, 예를 들어 연산자가 하나도 없이 숫자 하나만 입력될 때를 생각 못했다.

# <해결>
# 1.  각 문자들 사이에 괄호가 들어갈 자리를 마련한다.
#     입력 데이터가 3+8*7-9*2 이라면_3_+_8_*_7_-_9_*_2_  이런식으로 바꿔준다.
#     dfs를 통해 괄호가 들어갈 위치의 모든 조합을 구한다.
#     i가 0일 때를 예로 들면 i와 i+6번째를 괄호로 바꿔주고 (3_+_8)*_7_-_9_*_2_
#     재귀함수 dfs(i+8)를 통해서 다음 가능한 괄호 위치 인덱스로 가준다.
#     i+6이 입력데이터의 길이를 넘어가면, 즉 마지막 _를 넘어가면 해당 dfs는 그만한다.

# 2.  answer = int(-10e9)로 초기화한다.

# 3.  n=1일 때가 특수케이스이므로 따로 처리한다.

from collections import deque
answer = int(-10e9)
def calc(ls):
    global answer
    new_ls = []
    i=0
    while i < len(ls):
        if ls[i]=='(':
            temp = ls[i+1] + ls[i+3] + ls[i+5]
            new_ls.append(str(eval(temp)))
            i+=6
        else:
            if ls[i]!=' ' and ls[i]!=')':
                new_ls.append(ls[i])
        i+=1

    queue = deque(new_ls)
    num1 = queue.popleft()
    while queue:
        oper = queue.popleft()
        num2 = queue.popleft()
        num1 = str(eval(num1+oper+num2))
    answer = max(int(num1),answer)
        
def dfs(idx):
    for i in range(idx,len(ls),4):
        if i+6>=len(ls):
            break
        ls[i]='('
        ls[i+6]=')'
        calc(ls)
        dfs(i+8)
        ls[i]=' '
        ls[i+6]=' '  
    return
n = int(input())
text = input()
if n==1:
    print(text)
else:
    ls = ' '
    for i in text:
        ls+=i+' '
    ls = list(ls)
    dfs(0)
    print(answer)
