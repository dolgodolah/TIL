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
    queue = deque()
    cnt = 0
    visited = [[False]*8 for _ in range(8)]
    queue.append((0,0,start))
    visited[0][0]=True
    
    #8x8체스판의 (0,0)과 시작값이 다르면 색칠해야하므로 cnt+=1 하고 시작한다.
    if temp[0][0]!=start:
        cnt+=1

    while queue:
        x, y, value = queue.popleft()
        for i in range(4):
            if 0<=x+dx[i]<8 and 0<=y+dy[i]<8:
                nx = x+dx[i]
                ny = y+dy[i]
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    #해당 칸(x,y)의 값(value)과 인접한 칸(nx,ny)의 값이 서로 같은 색이면 색칠한다. 
                    if temp[nx][ny]==value:
                        cnt+=1
                        if temp[nx][ny] == 'W':
                            queue.append((nx,ny,'B'))
                        elif temp[nx][ny] == 'B':
                            queue.append((nx,ny,'W'))
                    #서로 다른 색이면 색칠할 필요가 없으므로 cnt는 증가X
                    else:
                        queue.append((nx,ny,temp[nx][ny]))

    return cnt

def bfs(x,y):
    temp = [[0]*8 for _ in range(8)]
    #8x8 크기로 잘라 temp에 담는다.
    for i in range(8):
        for j in range(8):
            temp[i][j]=graph[i+x][j+y]
    
    #8x8 체스판 색칠한 횟수 구하는데, 두 가지 경우의 수가 있다.
    #(0,0)이 W로 시작하는 경우, (0,0)이 B로 시작하는 경우이다.
    temp_answer = min(get_cnt(temp,'W'), get_cnt(temp,'B'))
    return temp_answer


answer = int(10e9)
for i in range(n):
    for j in range(m):
        if 0<=i+8<=n and 0<=j+8<=m:
            answer = min(bfs(i,j),answer)
print(answer)