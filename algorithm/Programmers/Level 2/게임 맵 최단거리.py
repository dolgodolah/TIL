from collections import deque
def solution(maps):
    answer = int(10e9)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    queue.append((0,0,1))
    visited=[[False]*len(maps[0]) for _ in range(len(maps))]
    visited[0][0]=True
    while queue:
        x,y,cnt=queue.popleft()
        if x==len(maps)-1 and y==len(maps[0])-1:
            answer=min(answer,cnt)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if visited[nx][ny]==False and maps[nx][ny]==1:
                    visited[nx][ny]=True
                    queue.append((nx,ny,cnt+1))
    if answer==int(10e9):
        return -1
    else:
        return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))