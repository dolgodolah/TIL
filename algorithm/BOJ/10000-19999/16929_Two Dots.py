# 백트래킹을 통해 순회를 확인하는 문제

# 백트래킹 문제인데 살짝 머리를 써야된다. 첫 시작 지점의 방문처리를 바로 하지않고 그 이후부터 해야된다.
# 근데 다음 dfs에서 바로 첫 시작점을 다시 방문하면? 그 때는 k가 4 이상이어야 한다는 조건(사이클 크기가 4이상)을 활용해서
# k>=4일때 첫 시작점을 다시 방문하면 정답을 갱신하는 풀이이다.

# 처음 푼 풀이는 4512ms 걸려서 다른 좋은 풀이 찾아봤다.
# 비슷한 풀이였으나 이 문제에 더 효율적으로 접근하는 방법이 있었다.
# 내 dfs는 해당 좌표에서 모~든 경로를 다 뒤져보다가 사이클이 되면 정답을 갱신하는 방법이다.
# 즉 visited[nx][ny]=True했다가 visited[nx][ny]=False했다가 하는 과정이 있다.

# 하지만 좋은 풀이는 해당 좌표에서 dfs를 통해 한 경로를 확인해보고 사이클이 형성 되지 않으면 어떤 경로도 사이클이 형성되지않는다는 것을 활용했다.
# 즉 visited[nx][ny]=False를 안해줘도 된다는 소리다.

# 10 10
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# AAAAAAAAAA
# 이 입력에서 차이를 느낄 수 있다. 내가 푼 풀이로 접근하면 수많은 경로를 다 가보는거다.
# 효율적인 풀이는 무슨 경로라도 하나만 가보고 사이클이 되면 answer=True, 안되면 해당 좌표의 dfs는 끝나는거다.


#효율적인 풀이
def dfs(x,y,color,k):
    global answer,visited
    global i,j
    if answer:
        return
    visited[x][y]=True
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==color:
                if visited[nx][ny]==False: #처음가는 경로이면 간다.
                    dfs(nx,ny,color,k+1)
                else:
                    if k>=3 and nx==i and ny==j: #사이클이 형성되는데 크기도 4이상이 되면 정답을 갱신하고 return한다.
                        answer=True
                        return
answer = False
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        visited = [[False]*m for _ in range(n)]
        dfs(i,j,graph[i][j],0)
        if answer:
            break
    if answer:
        break
if answer:
    print("Yes")
else:
    print("No")


#내가 푼 풀이
# from collections import deque
# def dfs(x,y,color,k):
#     global answer,visited
#     global i,j
#     if k>=4 and x==i and y==j: #k가 4이상인 사이클이 존재하면
#         answer = "Yes"
#         return True
#     for d in range(4):
#         nx = x+dx[d]
#         ny = y+dy[d]
#         if 0<=nx<n and 0<=ny<m:
#             if graph[nx][ny]==color and visited[nx][ny]==False:
#                 visited[nx][ny]=True
#                 dfs(nx,ny,color,k+1)
#                 visited[nx][ny]=False
# answer = "No"
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# n,m=map(int,input().split())
# graph=[]
# for _ in range(n):
#     graph.append(list(input()))

# for i in range(n):
#     for j in range(m):
#         visited = [[False]*m for _ in range(n)]
#         dfs(i,j,graph[i][j],0)
#         if answer=='Yes':
#             break
#     if answer=='Yes':
#         break
# print(answer)
