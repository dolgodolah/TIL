# 각 좌표마다 0부터 15까지의 값이 주어진다.
# 이 값들을 이진수로 바꾸면 0000~1111의 형태로 바뀌는데 이에 맞춰 dx,dy를 만들어준다.
# 이진수 중 1이면 벽, 0이면 통로이기때문에 0일 때만 이동할 수 있다.
# 성에 있는 방의 개수와 가장 넓은 방의 넓이는 위 조건들만 잘 고려해주면 된다.
# 하나의 벽을 제거하여 얻을 수 잇는 가장 넓은 방의 크기는
# 각 좌표값의 이진수들마다 1을 0으로 바꿔 bfs롤 진행시켜보았다. (성 밖을 나가는 경우 주의)

import sys
from collections import deque
input=sys.stdin.readline

#남,동,북,서
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def findPath(num):
    arr1=list(map(int,format(num,'b')))
    for _ in range(4-len(arr1)):
        arr1.insert(0,0)
    return arr1
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    cnt=0
    while queue:
        x,y=queue.popleft()
        cnt+=1
        path=findPath(graph[x][y])
        for i in range(len(path)):
            if path[i]==0: # 통로라면
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<m and 0<=ny<n and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
    return cnt


n,m=map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int,input().split())))

answer1=0
answer2=0
answer3=0
visited=[[False]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if visited[i][j]==False:
            answer1+=1
            visited[i][j]=True
            answer2=max(answer2,bfs(i,j))

ls=[8,4,2,1]
for i in range(m):
    for j in range(n):
        path=findPath(graph[i][j])
        #해당 좌표에서 벽들이 있으면 벽을 파괴해본다.
        for k in range(len(path)):
            if path[k]==1:
                visited=[[False]*n for _ in range(m)]
                visited[i][j]=True
                graph[i][j]-=ls[k]
                answer3=max(answer3,bfs(i,j))
                graph[i][j]+=ls[k]
            
print(answer1)
print(answer2)
print(answer3)