import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
board=[]
for _ in range(M):
    board.append(list(input().strip()))

white=0
blue=0
visited=[[False]*N for _ in range(M)]
def bfs(x,y,target):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    queue.append((x,y))
    result=0
    while queue:
        x,y=queue.popleft()
        result+=1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if visited[nx][ny]==False and board[nx][ny]==target:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
    return result
for i in range(M):
    for j in range(N):
        if visited[i][j]==False:
            visited[i][j]=True
            if board[i][j]=='W':
                white+=bfs(i,j,board[i][j])**2
            else:
                blue+=bfs(i,j,board[i][j])**2
print(white,blue)