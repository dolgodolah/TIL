#bfs를 통해 n*n만큼 탐색하여 이동횟수가 최대값보다 커질 때마다 answer을 갱신한다.
from collections import deque
T=int(input())
for t in range(1,T+1):
    n=int(input())
    board=[list(map(int,input().split())) for _ in range(n)]

    def bfs(x,y,num):
        global answer_cnt
        global answer_num
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        queue=deque()
        queue.append((x,y,1))
        while queue:
            x,y,cnt=queue.popleft()
            if answer_cnt<cnt:
                answer_cnt=cnt
                answer_num=num
            elif answer_cnt==cnt:
                if answer_num>num:
                    answer_num=num
                
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny]==board[x][y]+1:
                        queue.append((nx,ny,cnt+1))
        return
    answer_num=n*n
    answer_cnt=0
    for i in range(n):
        for j in range(n):
            bfs(i,j,board[i][j])

    print(f"#{t} {answer_num} {answer_cnt}")
