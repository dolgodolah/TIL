from collections import deque

n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(i,j,color):
    queue=deque()
    queue.append((i,j))
    visited[i][j]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
                nx,ny=x+dx[i],y+dy[i]
                if graph[nx][ny]==color and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny))


visited = [[False]*n for _ in range(n)]
answer1=0
answer2=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            bfs(i,j,graph[i][j])
            answer1+=1
        if graph[i][j]=='G':
            graph[i][j]='R'

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            bfs(i,j,graph[i][j])
            answer2+=1

print(answer1,answer2)