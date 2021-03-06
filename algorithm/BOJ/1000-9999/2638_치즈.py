from collections import deque
import sys

input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))


# 외부 공기에 2번 이상 접촉한 치즈들을 찾는다.
def find(): 
    queue=deque()
    queue.append((0,0)) # (0,0)은 무조건 공기이기 때문에 (0,0)부터 bfs를 수행한다.
    visited=[[False]*m for _ in range(n)]
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==0 and visited[nx][ny]==False: # 외부공기가 퍼지게 해주고 방문처리를 한다.
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                elif board[nx][ny]>0: # 외부공기가 치즈에 닿으면 +1을 해준다.
                    board[nx][ny]+=1

# bfs를 통해 갱신된 board값에 따라 처리를 해준다.
def melt():
    for i in range(n):
        for j in range(m):
            if board[i][j]>=3: # board[i][j] 값이 3이상인 치즈는 녹인다.(0으로 만든다.)
                board[i][j]=0
            elif board[i][j]==2: # 외부 공기와 2번 이상 만나지 않아 녹지 않은 치즈들은 다시 1로 초기화해준다.
                board[i][j]=1        

# 모든 치즈들이 녹았는지 확인한다.
def check():
    for i in board:
        if 1 in i:
            return False
    else:
        return True

answer=0
while True:
    answer+=1
    find()
    melt()
    if check(): #모든 치즈가 녹았으면 멈춘다.
        break

print(answer)
    
