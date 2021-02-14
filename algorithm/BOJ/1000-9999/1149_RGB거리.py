# 2차원리스트로 dp를 생성하고 각 조합에 대해 더 작은 값을 기록해나간다.
# 조심해야할건 인덱스 범위를 초과하지 않을때만 dp[i-1][j-1],dp[i-1][j+1]을 해주고
# 초과할때는 dp[i-1][j-1],dp[i-1][0]을 해준다.

import sys
input=sys.stdin.readline
n=int(input())
rgb = [[]]
for _ in range(n):
    rgb.append(list(map(int,input().split())))
dp = [[0]*3 for _ in range(n+1)]
dp[1][0],dp[1][1],dp[1][2]=rgb[1][0],rgb[1][1],rgb[1][2]
for i in range(1,n+1):
    for j in range(3):
        if j+1<3:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j+1])+rgb[i][j]
        else:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][0])+rgb[i][j]

print(min(dp[n]))
