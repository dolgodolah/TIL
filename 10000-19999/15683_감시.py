import sys
from copy import deepcopy
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
answer = int(10e9)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def set_cctv(x,y,direction,temp_graph):
    while True:
        if 0<=x+dx[direction]<n and 0<=y+dy[direction]<m:
            x = x + dx[direction]
            y = y + dy[direction]
            if temp_graph[x][y]==0: #사각지대(0)라면 시야를 밝힌다(9).
                temp_graph[x][y]=9
            elif temp_graph[x][y]==6: #벽(6)과 부딪히면 멈춘다.
                break
        else:
            break

def check(temp_graph):
    cnt = 0
    #사각지대의 수를 반환한다.
    for i in temp_graph:
        cnt += i.count(0)
    return cnt

def dfs(cnt):
    global answer
    if cnt==len(cctv):#cctv의 개수만큼 방향을 다 지정하면
        temp_graph = deepcopy(graph)
        for i in range(len(cctv)):
            x, y = cctv[i]#cctv마다 좌표값을 꺼낸다.
            if graph[x][y]==1:#해당 좌표에 있는 cctv가 1번cctv
                set_cctv(x,y,direction[i],temp_graph)
            elif graph[x][y]==2:#해당 좌표에 있는 cctv가 2번cctv
                set_cctv(x,y,direction[i],temp_graph)
                set_cctv(x,y,(direction[i]+2)%4,temp_graph)
            elif graph[x][y]==3:#해당 좌표에 있는 cctv가 3번cctv
                set_cctv(x,y,direction[i],temp_graph)
                set_cctv(x,y,(direction[i]+1)%4,temp_graph)
            elif graph[x][y]==4:#해당 좌표에 있는 cctv가 4번cctv
                set_cctv(x,y,direction[i],temp_graph)
                set_cctv(x,y,(direction[i]+1)%4,temp_graph)
                set_cctv(x,y,(direction[i]+2)%4,temp_graph)
        
        #모든 cctv로 사각지대를 제거했을 때 사각지대의 수가 최소값이면 answer을 갱신한다.
        answer = min(check(temp_graph),answer)
        return

    #cctv마다 방향 지정한다. 1~4번 CCTV는 4가지 경우의 수가 있다.
    for i in range(4):
        direction.append(i)
        dfs(cnt+1)
        direction.pop()

#1번~4번 cctv 좌표값 저장
cctv = []
direction = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 or graph[i][j]==2 or graph[i][j]==3 or graph[i][j]==4:
            cctv.append((i,j))

#5번 CCTV는 경우의 수가 하나밖에 없기때문에 사각지대 바로 제거한다.
for x in range(n):
    for y in range(m):
        if graph[x][y]==5:
            for i in range(4):
                nx,ny=x,y
                while True:
                    if 0<=nx+dx[i]<n and 0<=ny+dy[i]<m:
                        nx = nx+dx[i]
                        ny = ny+dy[i]
                        if graph[nx][ny]==0:
                            graph[nx][ny]=9
                        elif graph[nx][ny]==6:
                            break
                    else:
                        break

# for i in graph:
#     print(i)
dfs(0)
print(answer)