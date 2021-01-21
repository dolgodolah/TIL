#dfs와 메모이제이션을 활용한 문제이다.
#재귀 최대 깊이를 10**6으로 늘려도 recursionError가 떠서 10**9로 늘렸는데 메모리초과 뜬다;
#python으로 제출하니까 통과됐다.

from collections import deque
import sys
sys.setrecursionlimit(10**9)
def dfs(x,y):
    if not 0<=x<n or not 0<=y<m: #해당 칸(x,y)이 맵 밖(탈출)이라면 
        return 1
    if dp[x][y]!=-1: #해당 칸이 방문한 적 있는 칸이라면 그 칸의 탈출가능여부를 반환한다.
        return dp[x][y]
    dp[x][y]=0 #해당 칸(x,y) 방문처리

    #해당 칸(x,y)에서 가야하는 방향으로 dfs를 돌린다.
    direction = graph[x][y]
    if direction=='U':
        dp[x][y]=dfs(x-1,y)
    elif direction=='D':
        dp[x][y]=dfs(x+1,y)
    elif direction=='L':
        dp[x][y]=dfs(x,y-1)
    elif direction=='R':
        dp[x][y]=dfs(x,y+1)


    return dp[x][y]

n,m=map(int,input().split())
dp=[[-1]*m for _ in range(n)]
graph=[]
for _ in range(n):
    graph.append(list(input()))

answer = 0
for i in range(n):
    for j in range(m):
        answer+=dfs(i,j)
        # for k in dp:
        #     print(k)
        # print()
print(answer)
# for i in dp:
#     print(i)