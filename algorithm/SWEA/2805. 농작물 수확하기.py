# 농작물 수확하는 패턴이 넓이 우선 탐색 과정과 같기 때문에
# bfs를 통해 농작물을 수확하다가 중심으로부터 반경이 n//2를 넘어가면 return한다.

from collections import deque
def bfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    queue.append((x,y,0))
    visited=[[False]*n for _ in range(n)]
    visited[x][y]=True
    result=0
    while queue:
        x,y,cnt=queue.popleft()
        if cnt==n//2+1:
            return result
        result+=board[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny,cnt+1))
    return board[x][y]

T=int(input())
for t in range(1,T+1):
    n=int(input())
    board=[list(map(int,input())) for _ in range(n)]
    
    print(f"#{t} {bfs(n//2,n//2)}")