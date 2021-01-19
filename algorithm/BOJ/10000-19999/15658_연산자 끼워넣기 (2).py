# 주어진 연산자들의 조합을 백트래킹을 통해 구한다.
# 저번 연산자 끼워넣기(1)에서는 연산자들의 수가 딱맞게 주어져서
# permutations를 사용해도 시간초과가 뜨지않았지만
# 이번 문제에서는 연산자들이 더 많이 주어진다. 그 중에서 고르는거기때문에
# permutations를 사용하면 시간초과가 발생해서 백트래킹으로 다시 구현했다.
# 저번 문제도 다시 백트래킹으로 풀어보자.

import sys
from itertools import permutations
input = sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
operators=list(map(int,input().split())) #+,-,*,/

def dfs(cnt,result):
    global max_answer
    global min_answer
    if cnt==n-1: 
        max_answer=max(max_answer,result)
        min_answer=min(min_answer,result)
        return
    if operators[0]>0: #더하기
        operators[0]-=1
        dfs(cnt+1,result+nums[cnt+1])
        operators[0]+=1
    if operators[1]>0: #빼기
        operators[1]-=1
        dfs(cnt+1,result-nums[cnt+1])
        operators[1]+=1
    if operators[2]>0: #곱하기
        operators[2]-=1
        dfs(cnt+1,result*nums[cnt+1])
        operators[2]+=1
    if operators[3]>0: #나누기
        operators[3]-=1
        if result<0:
            result=abs(result)//nums[cnt+1]*(-1)
            dfs(cnt+1,result)
        else:
            dfs(cnt+1,result//nums[cnt+1])
        operators[3]+=1
min_answer = int(10e9)
max_answer = int(-10e9)
dfs(0,nums[0])
print(max_answer)
print(min_answer)
