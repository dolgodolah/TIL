# 최소비용을 구하라길래 bfs를 생각했다가 벽을 한 번 뚫을 수 있다는 조건때문에 모든 경우를 탐색하는 백트래킹(dfs)를 이용해야한다고 생각했다.
# 하지만 재귀호출최대범위를 벗어났고 setrecursionlimit을 통해 늘려도 여전히 에러가 발생했다.
# 답안코드를 보니 bfs를 이용했다...
# 각 좌표로 가는 최소비용을 기록하는 visited 테이블을 벽 뚫리지 않았을 때와 뚫렸을 때 두 개를 만들었다. -> visited=[[[0]*2] for _ in range(M)] for _ in range(N)]
# visited[x][y][0]에는 벽을 뚫지 않았을 때의 비용들을 갱신하고
# visited[x][y][1]에는 벽을 뚫었을 때의 비용을 갱신한다.

from collections import deque
N,M=map(int,input().split())
board=[]
for _ in range(N):
    board.append(list(map(int,input())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=int(10e9)

def bfs():
    queue=deque()
    queue.append((0,0,0)) #(x,y,벽뚫여부)
    visited=[[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0]=1
    while queue:
        x,y,check=queue.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][check]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny]==1 and check==0: #이동할 좌표가 벽이고, 벽이 뚫린 적 없을 때
                    visited[nx][ny][1]=visited[x][y][0]+1 #전 좌표까지의 비용+1
                    queue.append((nx,ny,1)) #check를 1로 바꿔준다.(뚫린적 있음.)
                elif board[nx][ny]==0 and visited[nx][ny][check]==0: #이동할 좌표가 빈 공간이고, 최초방문일 때
                    visited[nx][ny][check]=visited[x][y][check]+1
                    queue.append((nx,ny,check))

    return -1

print(bfs())