# 그리디 알고리즘 설명

# 파이프 설치는 최대한 위쪽으로 설치되어야 한다는 그리디 알고리즘을 기본으로 두고 풀이했다.
# . . . . .
# . . . . .
# . . . . .
# . . . . . 
# 이와같이 격자가 주어졌을 때 0행부터 탐색한다고 해보자.
# 0행0열에서 시작한 파이프가 3행4열로 연결되었다면 가장 적은 갯수(최악)의 파이프 설치가 된다.
# 즉, 0행부터 탐색했을 때는 마지막 열에서 최대한 위쪽 행으로 연결되어야 한다.

# +

# dfs 알고리즘 설명
# 백트래킹으로 접근하다보니 여기서 조금 시간이 걸렸었다.
# 그냥 깊이우선탐색으로 파이프를 설치할 수 있다면 끝까지 설치하고
# 끝 열에 도착하면 True를 return하여 해당 시작열은 파이프 설치가 가능하다는 걸 알린다.
# 즉 모든 행마다 dfs 탐색을 하여 파이프 설치가 가능한지 여부를 판단한다.


r,c=map(int,input().split())
board=[]
for _ in range(r):
    board.append(list(input()))

# ↗ → ↘
dx=[-1,0,1]
dy=[1,1,1] 
visited=[[False]*c for _ in range(r)]
def dfs(x,y,visited):
    if y==c-1:
        return True
    
    for i in range(3):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if visited[nx][ny]==False and board[nx][ny]=='.':
                visited[nx][ny]=True
                if dfs(nx,ny,visited):
                    return True
    return False
answer=0
for i in range(r):
    if dfs(i,0,visited):
        answer+=1
print(answer)
