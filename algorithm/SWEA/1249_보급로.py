# bfs를 통해 최종 목적지까지 최소비용을 구한다.
# value_graph에는 각 좌표값마다 비용 누적치를 저장한다.
# 방문처리를 응용해야하는데,
# 해당 좌표를 처음 방문했을 때는 평소처럼 하면되고
# 해당 좌표를 방문한적이 있더라도 비용 누적치가 더 낮은 값이 나오면 갱신해줘야한다.

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j):
    value_graph = [[-1]*n for _ in range(n)]
    queue = deque()
    queue.append((i,j,0))
    while queue:
        x,y,value = queue.popleft()
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
                nx = x+dx[i]
                ny = y+dy[i]
                if value_graph[nx][ny]==-1: # 처음 방문하는 도로이면
                    value_graph[nx][ny]=value+graph[nx][ny] # (nx,ny)까지 오는데 드는 비용 누적치는 전 도로까지의 누적치(value)와 해당 도로 값(graph[nx][ny])을 더한 값이 된다.
                    queue.append((nx,ny,value_graph[nx][ny]))

                else: # 방문한적 있는 도로이지만 
                    if value_graph[nx][ny]>value+graph[nx][ny]: # 전 도로까지의 누적치(value)와 해당 도로 값(graph[nx][ny])의 합이 (nx,ny)의 비용 누적치보다 작으면
                        value_graph[nx][ny]=value+graph[nx][ny] # (nx,ny)까지 오는데 드는 비용 누적치(value_graph[nx][ny])를 갱신한다.
                        queue.append((nx,ny,value_graph[nx][ny]))
    print(f"#{t} {value_graph[n-1][n-1]}")
                


T = int(input())
for t in range(1,T+1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input())))
    answer = int(10e9)
    visited = [[False]*n for _ in range(n)]   
    bfs(0,0)