# 비교적 쉬운 문제를 오랜만에 봐서 그런지 모든게 의심스럽다.
# 너무 쉬운데?라는 생각에 예외적인 경우를 찾으려 애를 쓰다가
# 모든 칸이 빈칸(상어 존재x)인 경우를 고려하여 제출했고 바로 통과했다.
# 하지만 다른 정답자 소스보니까 모든 칸이 빈칸인 경우는 고려안해줘도 된다.
# 문제를 다시 보니 'N×M 크기의 공간에 아기 상어 여러 마리가 있다'라고 했기때문에 무조건 상어는 있다고 보면 될 것 같다.

# 내 소스는 빈 칸마다 안전 거리를 구하여 안전 거리의 최댓값을 출력했다.
# 다른 소스보니까 상어를 기준으로 bfs를 실행하였다.
# 그러면 자연스럽게 안전 거리의 최댓값이 나온다.
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y,0))
    visited = [[False]*m for _ in range(n)]
    visited[x][y]=True
    while queue:
        x,y,d=queue.popleft()
        for i in range(8):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m:
                nx,ny=x+dx[i],y+dy[i]
                if visited[nx][ny]==False:
                    if graph[nx][ny]==0:
                        visited[nx][ny]=True
                        queue.append((nx,ny,d+1))
                    else: # 상어 발견하면 안전거리 반환하고 종료
                        return d+1
                
                
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0: #빈 칸마다 안전거리를 구한다.
            answer = max(answer,bfs(i,j))

print(answer)