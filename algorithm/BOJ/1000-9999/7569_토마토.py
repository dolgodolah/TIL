from collections import deque
import sys


input=sys.stdin.readline
m,n,h=map(int,input().split())
board=[[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        board[i].append(list(map(int,input().split())))

dx=[-1,1,0,0,0,0] #앞,뒤,좌,우,위,아래
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]

answer=0
tomato=[]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k]==1:
                tomato.append((i,j,k,0))


def bfs():
    global answer
    queue=deque(tomato)
    while queue:
        z,x,y,t=queue.popleft()
        answer=max(answer,t)
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if board[nz][nx][ny]==0:
                    board[nz][nx][ny]=1
                    queue.append((nz,nx,ny,t+1))
        

def check():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k]==0:
                    return False
    return True

bfs()
if check():
    print(answer)
else:
    print(-1)
