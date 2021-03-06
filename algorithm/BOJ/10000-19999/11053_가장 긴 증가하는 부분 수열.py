# j(0~i-1번째까지)번째 수와 i번째 수를 비교하여 증가하는 수열이 구성되면 dp[i]=max(dp[i],dp[j]+1)이 된다.


N=int(input())
ls=list(map(int,input().split()))
answer=0
dp=[1]*N
for i in range(1,N):
    for j in range(i):
        if ls[i]>ls[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))