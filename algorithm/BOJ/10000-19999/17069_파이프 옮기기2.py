# 기존에 풀었던 파이프 옮기기에서 데이터에 제한이 까다로워졌다.
# 원래 이 문제는 dp를 활용하여야 푸는 문제인데 파이프 옮기기1에서는 백트래킹을 통해 풀어도 시간초과가 뜨지 않았다.
# 이 문제에서는 dp로 풀어야 통과가 가능하다.

# dp에 각 좌표별로 (가로,대각선,세로)파이프가 몇 개 있는지 갱신할 것이다.
# 각 좌표를 가로로 왔을 때, 대각선으로 왔을 때, 세로로 왔을 때를 다 고려해준다.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]

dp[0][1][0]=1
for x in range(n):
    for y in range(n):
        #좌표 (x,y) 기준으로 가로 파이프를 놓을 수 있다면
        if y+1<n and graph[x][y+1]==0:
            dp[x][y+1][0] += dp[x][y][0]+dp[x][y][1] #(x,y)의 가로, 대각선 dp값을 더한다.
        
        #세로 파이프를 놓을 수 있다면
        if x+1<n and graph[x+1][y]==0:
            dp[x+1][y][2] += dp[x][y][2]+dp[x][y][1] #세로,대각선 dp값을 더한다.
        
        #대각선 파이프를 놓을 수 있다면
        if x+1<n and y+1<n and graph[x+1][y+1]==0 and graph[x+1][y]==0 and graph[x][y+1]==0:
            dp[x+1][y+1][1] += dp[x][y][0]+dp[x][y][1]+dp[x][y][2] #가로,세로,대각선 dp값을 더한다.

print(sum(dp[n-1][n-1]))