# 몇 일전에 풀었던 괄호 추가하기1의 연장선이다. 동일한 풀이지만 연산법칙이 달라졌다.
# 평소에 사용하는 연산법칙(+,-보다 * 먼저하는 연산)을 적용하면 되기 때문에 더 쉽다.
# answer이 초기값은 저번과 다르게 -10e9가 아닌 괄호를 안했을때의 연산 결과값으로 하면 된다.(보통의 연산법칙이기 때문에)

def calc(ls):
    global answer
    new_ls=""
    i=0
    #괄호부터 연산을 우선 적용한 결과를 new_ls에 담는다.
    while i<len(ls):
        if ls[i]=='(':
            temp = ls[i+1]+ls[i+3]+ls[i+5]
            new_ls+=str(eval(temp))
            i+=6
        elif not ls[i]=='(' and not ls[i]==')' and not ls[i]=='_':
            new_ls+=ls[i]
        i+=1
    
    #괄호 우선 연산 적용 후에는 일반 연산법칙과 동일하므로 eval로 처리한다.
    answer = max(answer,eval(new_ls))
    
def dfs(idx):
    for i in range(idx,len(ls),4):
        if i+6>=len(ls):
            break
        ls[i]='('
        ls[i+6]=')'
        calc(ls)
        dfs(i+8)
        ls[i]='_'
        ls[i+6]='_'

n=int(input())
data=input()
ls = '_'
for i in data:
    ls+=i+'_'

ls = list(ls)
answer = eval(data)
dfs(0)
print(answer)
