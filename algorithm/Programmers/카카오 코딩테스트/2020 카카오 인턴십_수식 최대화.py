# 21년 5월 8일 두번째 풀이
from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    new_expression=list()
    num=""
    for i in range(len(expression)):
        if expression[i] in ['0','1','2','3','4','5','6','7','8','9']:
            num+=expression[i]
        else:
            new_expression.append(num)
            new_expression.append(expression[i])
            num=""
    new_expression.append(num)
    # print(new_expression)

    for operations in permutations(['+','-','*'],3):
        copy_expression=new_expression.copy()
        
        for operation in operations:
            while operation in copy_expression:
                for i in range(len(copy_expression)):
                    if copy_expression[i]==operation:
                        tmp=""
                        for _ in range(3):tmp+=copy_expression.pop(i-1)
                        copy_expression.insert(i-1,str(eval(tmp)))
                        break
        answer=max(answer,abs(int(copy_expression[0])))

    return answer


# 21년 1월 26일 첫번째 풀이
from itertools import permutations
def solution(expression):
    answer = 0
    operator = set() #해당 expression에서 사용된 연산자의 종류를 나타낸다.

    ls = []
    temp = ''
    #expression의 숫자와 연산자 분리, 50*6-3*2 -> ['50','*','6','-','3']
    for i in expression:
        if i=='+' or i=='-' or i=='*':
            ls.append(temp)
            ls.append(i)
            temp=''
            operator.add(i)
        else:
            temp+=i
    ls.append(temp) #마지막 숫자 추가해주자!
    
    #연산자들의 종류로 만들 수 있는 우선순위를 permutations를 통해 구한다.
    #{'-','+','*'} -> ('-','+','*'),('-', '+', '*'),('*', '-', '+'),('*', '+', '-'),('+', '-', '*'),('+', '*', '-')
    for i in permutations(operator,len(operator)): 
        new_ls = ls.copy()
        for j in i: #해당 우선순위(i)일 때 1순위인것부터 차례로 연산을 수행한다.
            while j in new_ls: #연산할 차례인 연산자가 ls에 없을 때까지 수행한다.
                for k in range(len(new_ls)):
                    if new_ls[k]==j: #연산할 차례인 연산자를 발견하면 인덱스에 주의해서 pop해 계산해주자.
                        temp = str(eval(new_ls.pop(k-1)+new_ls.pop(k-1)+new_ls.pop(k-1)))
                        new_ls.insert(k-1,temp)
                        break
        
        answer = max(answer,abs(int(new_ls[0])))#해당 우선순위(i)일 때의 연산이 끝나면 answer을 갱신한다.
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))