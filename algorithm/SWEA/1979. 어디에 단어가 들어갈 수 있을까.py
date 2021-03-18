# bfs를 활용하는 문제였다. 맵을 탐색하여 빈 공간(1)을 발견하면 4방향에 대해서 bfs 탐색을 해본다.
# (x,y,direction)에 대해 방문처리를 해준다. bfs를 통해 탐색된 (x,y,direction)도 방문처리해준다.

from collections import deque
T=int(input())
for t in range(1,T+1):
    n,k=map(int,input().split())

    board=[list(map(int,input().split())) for _ in range(n)]

    def bfs(x,y,direction):
        queue=deque()
        queue.append((x,y,1))
        while queue:
            x,y,cnt=queue.popleft()
            nx=x+move[direction][0]
            ny=y+move[direction][1]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]==1 and not (nx,ny,direction) in visited:
                    visited.add((nx,ny,direction))
                    queue.append((nx,ny,cnt+1))
        return cnt
    move=[(-1,0),(1,0),(0,-1),(0,1)]
    answer=0
    visited=set()
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for direction in range(4):
                    if not (i,j,direction) in visited:
                        visited.add((i,j,direction))
                        if bfs(i,j,direction)==k:
                            answer+=1


    print(f"#{t} {answer}")