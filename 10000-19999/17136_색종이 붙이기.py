import sys
from copy import deepcopy
input = sys.stdin.readline
graph = []
for _ in range(10):
    graph.append(list(map(int,input().split())))
paper = [0]*6
def check(x,y,k,graph):
    #한 변의 길이가 k인 색종이가 1만 정확히 덮는지 확인
    for i in range(x,x+k):
        for j in range(y,y+k):
            if not 0<=i<10 or not 0<=j<10 or graph[i][j]!=1:
                return False
    for i in range(x,x+k):
        for j in range(y,y+k):
            graph[i][j]=0
    return True

def check2(graph):
    for i in graph:
        if i.count(1)>0:
            return False
    return True

def dfs(x,y,graph):
    global answer
    if y==10:
        dfs(x+1,0,graph)
        return
    if x==10:
        answer = min(sum(paper[1:6]),answer)
        return
    if graph[x][y]==1:
        for k in range(5,0,-1):
            if paper[k]<5 and check(x,y,k,graph)==True:
                paper[k]+=1
                dfs(x,y+k,graph)
                paper[k]-=1
                for i in range(x,x+k):
                    for j in range(y,y+k):
                        graph[i][j]=1
    else:
        dfs(x,y+1,graph)

answer = int(10e9)
dfs(0,0,graph)
if answer == int(10e9):
    print(-1)
else:
    print(answer)
