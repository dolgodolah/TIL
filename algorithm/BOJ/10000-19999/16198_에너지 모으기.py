import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int,input().split()))

answer = 0
def dfs(result):
    global answer
    if len(ls)==2:
        answer = max(answer,result)

    for i in range(1,len(ls)-1):
        temp = ls.pop(i)
        dfs(result+ls[i-1]*ls[i])
        ls.insert(i,temp)
dfs(0)
print(answer)