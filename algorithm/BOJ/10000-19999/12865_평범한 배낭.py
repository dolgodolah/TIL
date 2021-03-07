# 기본 배낭문제이다.
# dp테이블은 dp=[[0]*(최대 무게+1) for _ in range(물건 수+1)]로 생성한다.
# 물건 정보에 대해서도 n(물건 수)만큼 stuff에 받는다.
# i번째 물건에 대해서 1~최대 무게(k)까지 dp 알고리즘을 수행한다.
# i번째 물건의 무게가 현재 무게(1~k 중)보다 크면 dp[i-1][j] 값을 그대로 대입,
# 아니라면 dp[i-1]의 현재 무게(1~k)에서 i번째 물건의 무게를 뺀 [j-stuff[i][0]] + stuff[i][1](i번째 물건의 가치)와 dp[i-1][j] 중 큰 값을 대입

import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dp=[[0]*(k+1) for _ in range(n+1)]
stuff=[]
for _ in range(n):
    stuff.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v=stuff[i-1][0],stuff[i-1][1]
        if w>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)

print(dp[n][k])