#첫번째 풀이(1992ms) : 불이 켜져 있는 방을 나타내는 light, 방문여부를 나타내는 visited을 통해 bfs를 진행했다.

#두번째 풀이 (192ms) : room=[[[False,False] for _ in range(N+1)] for _ in range(N+1)]를 통해 bfs를 진행했다.
#[False,False] : 상하좌우로 이동한지 여부, 불이 켜져있는지 여부
import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[[] for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    x,y,a,b=map(int,input().split())
    graph[x][y].append((a,b))
room=[[[False,False] for _ in range(N+1)] for _ in range(N+1)]
room[1][1][0],room[1][1][1]=True,True 
answer=0
def bfs():
    global answer
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    queue=deque()
    queue.append((1,1))
    while queue:
        x,y=queue.popleft()
        for a,b in graph[x][y]:
            if room[a][b][0] and not room[a][b][1]: #(a,b)방을 상하좌우 이동으로 갈 수 있고, (a,b)방 불이 꺼져있을 때
                queue.append((a,b))
            room[a][b][1]=True #(a,b)방 불을 켠다.
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #불이 켜져있는 방으로만 이동할 수 있다.
            if 1<=nx<=N and 1<=ny<=N:
                if room[nx][ny][1] and not room[nx][ny][0]: #(a,b)방 불이 켜져있고, (a,b)방을 가본적 없을 때
                    queue.append((nx,ny))
                room[nx][ny][0]=True #(a,b)방을 상하좌우 이동으로 갈 수 있는 방으로 표시한다.

bfs()
for i in range(1,N+1):
    for j in range(1,N+1):
        if room[i][j][1]==True:
            answer+=1
print(answer)




# 첫번째 풀이
# import sys
# from collections import deque
# input=sys.stdin.readline
# N,M=map(int,input().split())
# graph=[[[] for _ in range(N+1)] for _ in range(N+1)]

# for _ in range(M):
#     x,y,a,b=map(int,input().split())
#     graph[x][y].append((a,b))

# light=[[False]*(N+1) for _ in range(N+1)]
# light[1][1]=True
# answer=1
# def bfs():
#     global answer
#     dx=[-1,1,0,0]
#     dy=[0,0,-1,1]
#     visited=set()
#     visited.add((1,1,1)) 
#     queue=deque()
#     queue.append((1,1))
#     while queue:
#         x,y=queue.popleft()
#         #(x,y)방에 있는 스위치로 (a,b)방 불켠다.
#         for a,b in graph[x][y]:
#             if light[a][b]==False:
#                 # print(x,y,a,b)
#                 light[a][b]=True
#                 answer+=1
        
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             #불이 켜져있는 방으로만 이동할 수 있다.
#             if 1<=nx<=N and 1<=ny<=N and light[nx][ny]==True and not (nx,ny,answer) in visited:
#                 visited.add((nx,ny,answer))
#                 queue.append((nx,ny))

# bfs()
# print(answer)

