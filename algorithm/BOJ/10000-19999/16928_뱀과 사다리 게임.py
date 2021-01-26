# 왜 처음에 방문처리를 안해도된다고 생각했을까?
# bfs로 접근했기때문에 해당 칸을 최초방문했을때가 그 칸까지 가는데 가장 빠른 방법이다.

from collections import deque
n,m=map(int,input().split())
graph=[0]*101

for _ in range(n):
    a,b=map(int,input().split())
    graph[a]=b
for _ in range(m):
    a,b=map(int,input().split())
    graph[a]=b

def bfs():
    queue = deque()
    queue.append((1,0)) #칸, 주사위 굴린 횟수
    visited = [False]*101
    visited[1]=True
    while queue:
        x,cnt=queue.popleft()
        if x==100:
            return cnt
        for i in range(1,7):
            if x+i<101:
                nx=x+i
                if visited[nx]==False:
                    if graph[nx]==0:
                        queue.append((nx,cnt+1))
                        visited[nx]=True
                    else:
                        queue.append((graph[nx],cnt+1))
                        visited[graph[nx]]=True

print(bfs())