# 해결 아이디어 자체는 쉽다. 근데 깔끔하게 구현하려면 머리를 굴려야돼서
# 그 시간에 빨리 푸는게 좋겠다 싶어 노가다로 빨리 구현했다.
# bfs로 그래프를 이동하는데 (x,y)에 있는 파이프 종류에 따라 이동할 수 있는 범위가 달라진다.
# 고려해야할 점은 result를 반환하게 되는 경우가 2가지인데
# 입력으로 주어진 시간이 다 지났을 때와 파이프에 막혀 더 이상 이동할 곳이 없을 때이다.

from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def go(x,y):
    result=0
    queue=deque()
    queue.append((x,y,1))
    visited=[[False]*m for _ in range(n)]
    visited[x][y]=True
    while queue:
        x,y,cnt=queue.popleft()
        result+=1
        if cnt>l: #시간이 지나서 끝나는 경우는 result-1을 해줘야한다.
            return result-1
        if graph[x][y]==1:
            if 0<=x-1<n:
                if graph[x-1][y]==1 or graph[x-1][y]==2 or graph[x-1][y]==5 or graph[x-1][y]==6:
                    if visited[x-1][y]==False:
                        visited[x-1][y]=True
                        queue.append((x-1,y,cnt+1))
            if 0<=x+1<n:
                if graph[x+1][y]==1 or graph[x+1][y]==2 or graph[x+1][y]==4 or graph[x+1][y]==7:
                    if visited[x+1][y]==False:
                        visited[x+1][y]=True
                        queue.append((x+1,y,cnt+1))
            if 0<=y-1<m:
                if graph[x][y-1]==1 or graph[x][y-1]==3 or graph[x][y-1]==4 or graph[x][y-1]==5:
                    if visited[x][y-1]==False:
                        visited[x][y-1]=True
                        queue.append((x,y-1,cnt+1))
            if 0<=y+1<m:
                if graph[x][y+1]==1 or graph[x][y+1]==3 or graph[x][y+1]==6 or graph[x][y+1]==7:
                    if visited[x][y+1]==False:
                        visited[x][y+1]=True
                        queue.append((x,y+1,cnt+1))
        elif graph[x][y]==2:
            if 0<=x-1<n:
                if graph[x-1][y]==1 or graph[x-1][y]==2 or graph[x-1][y]==5 or graph[x-1][y]==6:
                    if visited[x-1][y]==False:
                        visited[x-1][y]=True
                        queue.append((x-1,y,cnt+1))
            if 0<=x+1<n:
                if graph[x+1][y]==1 or graph[x+1][y]==2 or graph[x+1][y]==4 or graph[x+1][y]==7:
                    if visited[x+1][y]==False:
                        visited[x+1][y]=True
                        queue.append((x+1,y,cnt+1))
        elif graph[x][y]==3:
            if 0<=y-1<m:
                if graph[x][y-1]==1 or graph[x][y-1]==3 or graph[x][y-1]==4 or graph[x][y-1]==5:
                    if visited[x][y-1]==False:
                        visited[x][y-1]=True
                        queue.append((x,y-1,cnt+1))
            if 0<=y+1<m:
                if graph[x][y+1]==1 or graph[x][y+1]==3 or graph[x][y+1]==6 or graph[x][y+1]==7:
                    if visited[x][y+1]==False:
                        visited[x][y+1]=True
                        queue.append((x,y+1,cnt+1))
        elif graph[x][y]==4:
            if 0<=x-1<n:
                if graph[x-1][y]==1 or graph[x-1][y]==2 or graph[x-1][y]==5 or graph[x-1][y]==6:
                    if visited[x-1][y]==False:
                        visited[x-1][y]=True
                        queue.append((x-1,y,cnt+1))
            if 0<=y+1<m:
                if graph[x][y+1]==1 or graph[x][y+1]==3 or graph[x][y+1]==6 or graph[x][y+1]==7:
                    if visited[x][y+1]==False:
                        visited[x][y+1]=True
                        queue.append((x,y+1,cnt+1))
        elif graph[x][y]==5:
            if 0<=x+1<n:
                if graph[x+1][y]==1 or graph[x+1][y]==2 or graph[x+1][y]==4 or graph[x+1][y]==7:
                    if visited[x+1][y]==False:
                        visited[x+1][y]=True
                        queue.append((x+1,y,cnt+1))
            if 0<=y+1<m:
                if graph[x][y+1]==1 or graph[x][y+1]==3 or graph[x][y+1]==6 or graph[x][y+1]==7:
                    if visited[x][y+1]==False:
                        visited[x][y+1]=True
                        queue.append((x,y+1,cnt+1))
        elif graph[x][y]==6:
            if 0<=x+1<n:
                if graph[x+1][y]==1 or graph[x+1][y]==2 or graph[x+1][y]==4 or graph[x+1][y]==7:
                    if visited[x+1][y]==False:
                        visited[x+1][y]=True
                        queue.append((x+1,y,cnt+1))
            if 0<=y-1<m:
                if graph[x][y-1]==1 or graph[x][y-1]==3 or graph[x][y-1]==4 or graph[x][y-1]==5:
                    if visited[x][y-1]==False:
                        visited[x][y-1]=True
                        queue.append((x,y-1,cnt+1))
        elif graph[x][y]==7:
            if 0<=x-1<n:
                if graph[x-1][y]==1 or graph[x-1][y]==2 or graph[x-1][y]==5 or graph[x-1][y]==6:
                    if visited[x-1][y]==False:
                        visited[x-1][y]=True
                        queue.append((x-1,y,cnt+1))
            if 0<=y-1<m:
                if graph[x][y-1]==1 or graph[x][y-1]==3 or graph[x][y-1]==4 or graph[x][y-1]==5:
                    if visited[x][y-1]==False:
                        visited[x][y-1]=True
                        queue.append((x,y-1,cnt+1))
    return result #갈 곳이 없어서 끝나는 경우에는 그대로 result 반환

T = int(input())
for t in range(1,T+1):
    n,m,r,c,l=map(int,input().split())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    print(f"#{t} {go(r,c)}")
    