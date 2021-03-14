# bfs, dfs 알고리즘을 이용해 풀 수 있다. 숫자길이가 7이 되면 set에 add한다.
# 격자의 크기가 4x4라서 시간초과는 발생하지 않았다.

from collections import deque
test_case=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j):
    queue=deque()
    queue.append((i,j,board[i][j],1))
    while queue:
        x,y,num,cnt=queue.popleft()
        if cnt==7:
            answer.add(num)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<4 and 0<=ny<4 and cnt<7:
                queue.append((nx,ny,num+board[nx][ny],cnt+1))

def dfs(x,y,num):
    if len(num)==7:
        answer.add(num)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx,ny,num+board[nx][ny])

for t in range(1,test_case+1):
    board=[list(map(str,input().split())) for _ in range(4)]
    answer=set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,board[i][j])
    print(f"#{t} {len(answer)}")
