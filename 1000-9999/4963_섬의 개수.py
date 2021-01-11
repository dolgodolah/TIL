import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    graph[i][j]=0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            if 0<=x+dx[i]<h and 0<=y+dy[i]<w:
                nx = x+dx[i]
                ny = y+dy[i]
                if graph[nx][ny] == 1:
                    graph[nx][ny]=0
                    queue.append((nx,ny))


while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    answer = 0
    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:# 해당 좌표가 땅이면 bfs를 통해 이어져있는 땅을 찾아 방문처리해준다.
                answer+=1
                bfs(i,j)
    print(answer)