# N의 최대범위가 <=6이기 때문에 "이 문제는 구현만 하면 되겠구나!" 싶어서 시간초과는 고려하지 않고 쉽게 풀었다.
# dfs를 통해 장애물 3개를 놓을 수 있는 모든 경우를 탐색하고 그 경우들마다 학생들 감시를 할 수 있는지 check한다.
# check 함수는 bfs로 구현하였다.
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(str,input().split())))

def check():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(N):
        for j in range(N):
            if graph[i][j]=='T':
                queue=deque()
                for direction in range(4):
                    queue.append((i,j,direction))
                visited=[[False]*N for _ in range(N)]
                visited[i][j]=True
                while queue:
                    x,y,direction=queue.popleft()
                    if graph[x][y]=='S':
                        return False # 선생님이 학생을 찾았다!
                    nx=x+dx[direction]
                    ny=y+dy[direction]
                    if 0<=nx<N and 0<=ny<N:
                        if graph[nx][ny]!='O' and visited[nx][ny]==False:
                            visited[nx][ny]=True
                            queue.append((nx,ny,direction))
    return True # 선생님이 학생을 찾을 수 없다.


def dfs(cnt):
    global answer
    if cnt==3:
        if check():
            answer=True
        return
    
    for i in range(N):
        for j in range(N):
            if graph[i][j]=='X':
                graph[i][j]='O'
                dfs(cnt+1)
                graph[i][j]='X'
answer=False
dfs(0)
if answer:
    print("YES")
else:
    print("NO")