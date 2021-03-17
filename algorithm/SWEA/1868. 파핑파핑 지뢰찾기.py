# 첫번째 아이디어 : 최소 몇 번의 클릭을 해야하는지 구해야하기 위해 백트래킹으로 구현하려 했다.
# 두번째 아이디어(채택) : 백트래킹으로 모든 클릭의 경우를 다 탐색하지 않아도 최소한의 클릭을 정의할 수 있었다.
# 지뢰의 위치를 이미 알고있기 때문에 8방향에 지뢰가 적은 것부터(0개~8개) 클릭하면 최소한의 클릭을 할 수 있다.

# 클릭할 수 있는 곳의 좌표와 8방향의 지뢰개수를 point 리스트에 (x,y,지뢰개수)의 형태로 삽입하고 board[x][y]=지뢰개수로 갱신한다.
# point리스트를 지뢰개수 기준으로 오름차순 정렬하고 오름차순으로 클릭해야할 곳(visited)만 click()을 수행한다.
# click() 함수 내에서는 해당 클릭 위치가 0인 경우 8방향을 다시 queue에 넣고 visited=True 처리 해주어 클릭을 하지 않아도 되도록 한다. (8방향 중 또 0이면 이 과정 반복)
from collections import deque
T=int(input())
for t in range(1,T+1):
    n=int(input())
    board=[list(input()) for _ in range(n)]
    dx=[-1,1,0,0,1,1,-1,-1]
    dy=[0,0,-1,1,-1,1,-1,1]
    point=[]
    for x in range(n):
        for y in range(n):
            if board[x][y]=='.':
                board[x][y]=0
                for i in range(8):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]=='*':
                        board[x][y]+=1
                point.append((x,y,board[x][y]))
    point.sort(key=lambda x:x[2])
    visited=[[False]*n for _ in range(n)]

    def click(x,y):
        queue=deque()
        queue.append((x,y))
        while queue:
            x,y=queue.popleft()
            if board[x][y]==0:
                for i in range(8):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                        queue.append((nx,ny))
                        visited[nx][ny]=True
    answer=0
    for x,y,value in point:
        if visited[x][y]==False:
            visited[x][y]=True
            click(x,y)
            answer+=1

        # for i in board:
        #     print(i)
        # print()
    print(f"#{t} {answer}")
