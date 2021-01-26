from collections import deque

n=int(input())
r1,c1,r2,c2=map(int,input().split())
dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]
def dfs():
    queue=deque()
    queue.append((r1,c1,0))
    visited=[[False]*n for _ in range(n)]
    visited[r1][c1]=True
    while queue:
        x,y,cnt=queue.popleft()
        if x==r2 and y==c2:
            return cnt
        for i in range(6):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
                nx,ny=x+dx[i],y+dy[i]
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny,cnt+1))
    return -1

print(dfs())