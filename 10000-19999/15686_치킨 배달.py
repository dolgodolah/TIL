import sys
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
queue=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            queue.append((i,j))

chicken = []
def calc(chicken):
    total = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                distance = int(10e9)
                for x,y in chicken:
                   distance = min(abs(i-x) + abs(j-y),distance)
                total += distance
    return total
def dfs(cnt,start):
    global answer
    if cnt==m:
        #치킨 거리 계산
        answer = min(calc(chicken),answer)
    
    for i in range(start,len(queue)):
        chicken.append(queue[i])
        dfs(cnt+1,i+1)
        chicken.pop()
answer = int(10e9)
dfs(0,0)



# for i in combinations(queue,m):
#     answer = min(calc(i),answer)
print(answer)