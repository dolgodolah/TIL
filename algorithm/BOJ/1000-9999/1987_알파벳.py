# 문제 풀이 접근 자체는 쉽다. 
# 첫번째 시도 visited=set() -> 시간 초과
# 두번째 시도 visited=dict() -> 시간 초과
# 세번째 시도 visited=[0]*26 -> 5192ms 통과

# 이 문제 자체가 파이썬에서 시간이 오래걸리는 것 같다.
# 5192ms도 평균인 느낌?
# 1000ms 이하대로 통과한 코드는 bfs로 접근한 것 같다.
R,C=map(int,input().split())
board=[]
for _ in range(R):
    board.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[0]*26
visited[ord(board[0][0])-65]=1
answer=0
def dfs(x,y,visited,cnt):
    global answer
    # print(x,y,cnt)
    answer=max(answer,cnt)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if visited[ord(board[nx][ny])-65]==0:
                visited[ord(board[nx][ny])-65]=1
                dfs(nx,ny,visited,cnt+1)
                visited[ord(board[nx][ny])-65]=0

dfs(0,0,visited,1)
print(answer)
