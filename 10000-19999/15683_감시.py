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
            nx = x + dx[direction]
            ny = y + dy[direction]
            if temp_graph[nx][ny]==0:
                temp_graph[nx][ny]=9
            elif temp_graph[nx][ny]==6:
                break
            # elif 1<=temp_graph[nx][ny]<=5:
            #     continue
            x,y=nx,ny
        else:
            break

def check(temp_graph):
    cnt = 0
    for i in temp_graph:
        cnt += i.count(0)
    return cnt

def dfs(cnt):
    global answer
    if cnt==len(cctv):#cctv의 개수만큼 방향을 다 지정하면
        temp_graph = deepcopy(graph)
        for i in range(len(cctv)):
            x, y = cctv[i]
            if graph[x][y]==1:
                set_cctv(x,y,direction[i],temp_graph)
            elif graph[x][y]==2:
                set_cctv(x,y,direction[i],temp_graph)
                set_cctv(x,y,(direction[i]+2)%4,temp_graph)
            elif graph[x][y]==3:
                set_cctv(x,y,direction[i],temp_graph)
                set_cctv(x,y,(direction[i]+1)%4,temp_graph)
            elif graph[x][y]==4:
                set_cctv(x,y,direction[i],temp_graph)
                set_cctv(x,y,(direction[i]+1)%4,temp_graph)
                set_cctv(x,y,(direction[i]+2)%4,temp_graph)
        
        answer = min(check(temp_graph),answer)
        return

    for i in range(4):#cctv마다 방향 지정
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

for x in range(n):
    for y in range(m):
        if graph[x][y]==5:
            for i in range(4):
                tx,ty=x,y
                while True:
                    if 0<=tx+dx[i]<n and 0<=ty+dy[i]<m:
                        nx = tx+dx[i]
                        ny = ty+dy[i]
                        if graph[nx][ny]==0:
                            print(nx,ny)
                            graph[nx][ny]=9
                        elif graph[nx][ny]==6:
                            break
                        tx,ty=nx,ny
                    else:
                        break

for i in graph:
    print(i)
dfs(0)
print(answer)