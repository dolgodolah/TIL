# 첫 아이디어 : 거울('/','\')을 백트래킹을 통해 빈 공간에 놓으려 했다. 거울 위치가 터무니없어도 두 C가 만나는지 확인하는 불필요한 과정이 많이 진행된다.

# 첫번째 시도(1460ms) : x,y,direction를 나타내는 3차원 visited배열을 통해 bfs 탐색을 했다. visited[x][y][direction]에는 해당 좌표까지 오는데 사용된 거울의 갯수가 된다.
# 즉, 해당 좌표 x,y를 최소의 거울이 사용됐을 때만 방문할 수 있도록 한다. 탐색 과정에서 목적지 C를 도착하면 그 때의 cnt가 최솟값일 경우 answer을 갱신한다.
# 좋은 풀이보다 시간이 걸리는 이유는 4방향마다 넓이우선탐색을 진행하여 목적지 C까지 도착할 수 있는 모든 경우를 탐색해서 그런것 같다.

# 두번째 시도(176ms) : visited를 4방향으로 처리하는게 아니라 무슨 방향이든 해당 좌표의 visited값보다 높을 때 방문하면 탐색을 멈추도록 한다.
# visited를 이렇게 처리하게되면 목적지 C까지 도착하게 되는 모든 경우가 아닌 최소의 경우만 visited를 갱신한다.


import sys
from collections import deque
input=sys.stdin.readline
W,H=map(int,input().split())

board=list()
for _ in range(H):
    board.append(list(input().strip()))

C=[]
for i in range(H):
    for j in range(W):
        if board[i][j]=='C':
            C.append((i,j))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[int(10e9)]*W for _ in range(H)]
def bfs():
    queue=deque()
    queue.append((C[0][0],C[0][1]))
    visited[C[0][0]][C[0][1]]=-1
    while queue:
        x,y=queue.popleft()
        print(x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            while 0<=nx<H and 0<=ny<W:
                if board[nx][ny]=='*':
                    break
                if visited[nx][ny]<visited[x][y]+1:
                    break
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))
                nx=nx+dx[i]
                ny=ny+dy[i]

bfs()
print(visited[C[1][0]][C[1][1]])

