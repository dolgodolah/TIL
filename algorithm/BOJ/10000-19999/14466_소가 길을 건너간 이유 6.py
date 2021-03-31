# 첫번째 풀이(2592ms) : 두 소가 한 쌍일 때 주어진 소들로 조합할 수 있는 모든 쌍들에 대해서 bfs를 통해 길을 건너지 않으면 만날 수 없는지 확인했다.
# 두번째 풀이(332ms) : 조합으로 만들어질 수 있는 모든 쌍(K!/2!개)에 대해서 bfs를 실행하는 것이 아닌 주어진 소(K개)들에 대해서만 bfs를 실행하였다.
# 문제에서 원하는 최종답은 길 건너지 않으면 만날 수 없는 소가 몇 쌍인지 구하는 것이다. 이는 소들마다 만날 수 없는 소가 몇마리인지 다 더하고 2로 나눠주면 된다.
from collections import deque
from itertools import combinations


N,K,R=map(int,input().split())
road=[[[] for _ in range(N+1)] for _ in range(N+1)]


for _ in range(R):
    a,b,c,d=map(int,input().split())
    road[a][b].append((c,d))
    road[c][d].append((a,b))

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited=[[False]*(N+1) for _ in range(N+1)]
    visited[x][y]=True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<nx<=N and 0<ny<=N:
                if visited[nx][ny]==False and not (nx,ny) in road[x][y]:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    if board[nx][ny]==True:
                        cnt+=1
    return K-1-cnt # K마리 소 - 자기 자신(1) - 만난 횟수 = 길을 건너지 않으면 만날 수 없는 소들 수

answer=0                    

# K마리 소들의 위치 정보를 입력한다.
cows=list()
board=[[False]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a,b=map(int,input().split())
    cows.append((a,b))
    board[a][b]=True #두번째 풀이를 위해서는 소가 위치한 좌표값에 True를 대입한 리스트를 만들어야한다.

answer=0
for cow in cows:
    x,y=cow
    answer+=bfs(x,y)
print(answer//2)

# 첫번째 풀이
# # K마리 소들로 이룰 수 있는 쌍들의 조합을 combinations을 통해 구현한다.
# for cow in combinations(cows,2):
#     start_x,start_y,end_x,end_y=cow[0][0],cow[0][1],cow[1][0],cow[1][1]
#     if not bfs(start_x,start_y,end_x,end_y): # 2마리의 해당 쌍이 길없이 만날 수 있는지 확인한다.
#         answer+=1
# print(answer)

