import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,0,1]
dy = [0,-1,1,0]
shark = []

#상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            shark=[i,j,2]
            break

def bfs(i,j):
    queue = deque()
    target = []
    visited = [[False]*n for _ in range(n)]
    queue.append((shark[0],shark[1],shark[2],0))
    visited[shark[0]][shark[1]] = True
    while queue:
        x,y,size,distance = queue.popleft()
        for k in range(4):
            #맵밖을 벗어나지 않고 상어가 이동할 수 있는 좌표이고 방문한적 없는 좌표이면
            if 0<=x+dx[k]<n and 0<=y+dy[k]<n and 0<=graph[x+dx[k]][y+dy[k]]<=size and visited[x+dx[k]][y+dy[k]]==False:
                nx,ny = x+dx[k],y+dy[k]
                visited[nx][ny]=True
                queue.append((nx,ny,size,distance+1))
                #상어가 먹이 사냥을 할 수 있는 좌표이면 타겟에 추가
                if 1<=graph[nx][ny]<size:
                    if target:
                        if target[0][2]==distance+1:
                            target.append((nx,ny,distance+1))
                    else:
                        target.append((nx,ny,distance+1))
    if target:
        target.sort()
        return target[0]
    else:
        return False

answer = 0
exp = 0
def find():
    global answer
    global exp
    while True:
        val = bfs(shark[0],shark[1])
        if val==False:
            #먹을 게 없어
            break
        else:
            exp+=1
            graph[shark[0]][shark[1]] = 0
            shark[0],shark[1] = val[0],val[1]
            graph[shark[0]][shark[1]] = 9
            if exp == shark[2]:
                shark[2]+=1
                exp=0
            answer+=val[2]

            # print("현재 물고기 크기 : ",shark[2],"exp :",exp)
            # for i in graph:
            #     print(i)
            # print()

find()
print(answer)