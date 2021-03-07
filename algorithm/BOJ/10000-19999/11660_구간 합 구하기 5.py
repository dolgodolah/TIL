# 다이나믹 프로그래밍 알고리즘을 이용해 배열의 누적합을 구한다.
# 주어진 좌표와 누적합을 이용하면 원하는 구간의 합을 구할 수 있다.
# dp[x2][y2]는 (0,0)에서 (x2,y2)까지의 합이다. 이 값에서 dp[x1-1][y2]와 dp[x2][y1-1]를 빼준다.
# dp[x1-1][y2]와 dp[x2][y1-1]에 중복되어 두번 빼진 값이 있다.(dp[x1-1][y1-1])
# 이 값을 더해주면 최종적으로 (x1,y1)에서 (x2,y2)까지의 구간합을 구할 수 있다.

import sys, copy
input=sys.stdin.readline
n,m=map(int,input().split())
array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=array[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]


for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])