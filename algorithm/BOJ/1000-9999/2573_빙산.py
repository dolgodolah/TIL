# 첫번째 시도 (실패) : 2636번 치즈(https://www.acmicpc.net/problem/2636)처럼 bfs 탐색 한번으로
# 1년동안 빙산이 녹는 과정을 구현하려 했다. (0,0)은 무조건 물이기 때문에 (0,0)부터 bfs 탐색을 시작했다. -> 탐색하는 칸이 0보다 클 때 -1을 해줌으로써 녹는 과정을 구현.

# 두번째 시도 (2844ms) : bfs 탐색 한번으로 구현이 잘 안되길래 해당 칸이 0(물)이면 방문처리와 bfs 탐색을 하여
# 빙산(board)과 동일한 크기의 tmp에 녹는 양을 갱신한다. 이 과정이 끝나면 melt()를 통해 board[i][j]-=tmp[i][j]를 한다.
# 빙산 조각의 갯수를 세는 것도 bfs를 통해 구현할 수 있다.

# 세번째 시도 (512ms) : bfs 탐색 한번만 해도 1년동안 빙산 녹는 과정 구현할 수 있었다. 해당 칸이 0(물)일 때 bfs탐색 하는것이 아닌
# 해당 칸이 빙하(1이상)일 때 bfs 탐색을 하면 된다. 주의할 점은 방문처리이다.
# bfs탐색을 하면서 탐색하는 칸 board[nx][ny]이 빙하(1이상)이면 탐색한 칸을 방문처리와 queue에 추가를 해주고
# 탐색하는 칸 board[nx][ny]이 0(물)이라면 4방향 탐색 전 칸 board[x][y]의 값을 -1 해준다.



import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
board=list()
for _ in range(n):
    board.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j):
    global visited
    queue=deque()
    queue.append((i,j))
    visited[i][j]=True
    while queue:
        x,y=queue.popleft()
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                #상하좌우 탐색하려는 칸이 빙하라면 방문처리를 해주고 queue에 추가한다.
                if board[nx][ny]>0: 
                    visited[nx][ny]=True
                    queue.append((nx,ny))

                #해당 칸이 빙하가 남아있고, 상하좌우 탐색하려는 칸이 물이라면 빙하를 -1 녹인다.
                elif board[nx][ny]==0 and board[x][y]>0:
                    board[x][y]-=1

day=0
while True:
    cnt=0
    visited=[[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            #방문처리를 해줌으로써 분리된 빙하조각들이 몇 개인지 확인할 수 있다.
            if board[i][j]!=0 and visited[i][j]==False:
                bfs(i,j)
                cnt+=1
    if cnt>=2:
        break
    if cnt==0:
        day=0
        break
    day+=1
    
print(day)
