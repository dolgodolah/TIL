import sys
from collections import deque

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
m,n=map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i,j,0))
answer = 0
def bfs():
    global answer
    while queue:
        x,y,cnt = queue.popleft()
        answer = max(answer,cnt)
        for i in range(4):
            if -1<x+dx[i]<n and -1<y+dy[i]<m:
                nx,ny = x+dx[i],y+dy[i]
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    queue.append((nx,ny,cnt+1))
def check():
    global answer
    for i in graph:
        if 0 in i:
            answer = -1
            break

bfs()
check()
print(answer)