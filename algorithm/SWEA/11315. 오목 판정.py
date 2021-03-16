#dfs풀이
def dfs(x,y,cnt):
    global answer
    # print(x,y,cnt)
    if cnt>=5:
        answer=True
        return
    if 0<=x+dx[direction]<n and 0<=y+dy[direction]<n and board[x+dx[direction]][y+dy[direction]]=='o':
        dfs(x+dx[direction],y+dy[direction],cnt+1)
    return

T=int(input())
for t in range(1,T+1):
    n=int(input())
    board=[list(input()) for _ in range(n)]
    dx=[-1,1,0,0,1,1,-1,-1]
    dy=[0,0,-1,1,1,-1,1,-1]

    answer=False
    for i in range(n):
        for j in range(n):
            if board[i][j]=='o':
                for direction in range(8):
                    dfs(i,j,1)
                if answer:
                    break
        if answer:
            break
    
    if answer:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")



# bfs풀이
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y,1))
    while queue:
        x,y,cnt=queue.popleft()
        if cnt==5:
            return True
        nx=x+dx[direction]
        ny=y+dy[direction]
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny]=='o':
                queue.append((nx,ny,cnt+1))
    return False
T=int(input())
for t in range(1,T+1):
    n=int(input())
    board=[list(input()) for _ in range(n)]
    dx=[-1,1,0,0,1,1,-1,-1]
    dy=[0,0,-1,1,1,-1,1,-1]

    answer=False
    for i in range(n):
        for j in range(n):
            if board[i][j]=='o':
                for direction in range(8):
                    if bfs(i,j):
                        answer=True
                if answer:
                    break
        if answer:
            break
    
    if answer:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")