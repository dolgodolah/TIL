import sys
from collections import deque
from copy import deepcopy
# input = sys.stdin.readline
n,m = map(int,input().split())
graph=[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(str,input())))

def get_cnt(temp,start):
    temp_graph = deepcopy(temp)
    queue = deque()
    cnt = 0
    visited = [[False]*8 for _ in range(8)]
    queue.append((0,0,start))
    if temp_graph[0][0]!=start:
        cnt+=1
        temp_graph[0][0]=start
    visited[0][0]=True
    
    while queue:
        x, y, value = queue.popleft()
        for i in range(4):
            if 0<=x+dx[i]<8 and 0<=y+dy[i]<8:
                nx = x+dx[i]
                ny = y+dy[i]
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    if temp_graph[nx][ny]==value:
                        cnt+=1
                        if temp_graph[nx][ny] == 'W':
                            temp_graph[nx][ny] = 'B'
                            queue.append((nx,ny,'B'))
                        elif temp_graph[nx][ny] == 'B':
                            temp_graph[nx][ny] = 'W'
                            queue.append((nx,ny,'W'))
                    else:
                        queue.append((nx,ny,temp[nx][ny]))

    return cnt

def bfs(x,y):
    
    temp = [[0]*8 for _ in range(8)]
    #8x8 크기로 잘라 temp에 담는다.
    for i in range(8):
        for j in range(8):
            temp[i][j]=graph[i+x][j+y]
    
    #8x8 체스판 색칠한 횟수 구한다.
    temp_answer = min(get_cnt(temp,'W'), get_cnt(temp,'B'))
    return temp_answer


answer = int(10e9)
for i in range(n):
    for j in range(m):
        if 0<=i+8<=n and 0<=j+8<=m:
            answer = min(bfs(i,j),answer)
print(answer)