import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited = [[False]*m for _ in range(n)]
    visited[x][y]=True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m:
                nx,ny=x+dx[i],y+dy[i]
                if graph[nx][ny]==1:
                    graph[nx][ny]=2
                elif graph[nx][ny]==0 and visited[nx][ny]==False:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
def remove():
    for i in range(n):
        for j in range(m):
            if graph[i][j]==2:
                graph[i][j]=0
def check():
    last_cheeze = 0
    for i in graph:
        last_cheeze += i.count(1) + i.count(2)
    return last_cheeze

cnt = 0
val = 0
while True:
    last_cheeze = val
    val = check()
    if val>0:
        cnt+=1
        bfs(0,0)
        remove()
    else:
        break

print(cnt)
print(last_cheeze)
