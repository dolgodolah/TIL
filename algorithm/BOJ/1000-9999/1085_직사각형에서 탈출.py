from collections import deque

x,y,w,h=map(int,input().split())
board=[[0]*(w+1) for _ in range(h+1)]
board[y][x]=1
# for i in board:
#     print(i)

dy=[-1,1,0,0]
dx=[0,0,-1,1]
queue=deque()
queue.append((y,x,0))
visited=[[False]*(w+1) for _ in range(h+1)]
visited[y][x]=True
answer=0
while queue:
    y,x,cnt=queue.popleft()
    if y==0 or x==0 or y==h or x==w:
        answer=cnt
        break
    for i in range(4):
        if 0<=y+dy[i]<h+1 and 0<=x+dx[i]<w+1:
            ny=y+dy[i]
            nx=x+dx[i]
            if visited[ny][nx]==False:
                visited[ny][nx]=True
                queue.append((ny,nx,cnt+1))
print(answer)