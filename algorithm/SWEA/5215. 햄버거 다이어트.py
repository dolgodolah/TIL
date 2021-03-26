#기본 배낭(knapsack)문제
T=int(input())
for idx in range(1,T+1):
    N,L=map(int,input().split())
    material=list()
    for _ in range(N):
        t,k=map(int,input().split()) #맛점수, 칼로리
        material.append((t,k))
    dp=[[0]*(L+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,L+1):
            t,k=material[i-1][0],material[i-1][1]
            if k>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-k]+t)
    
    print(f"#{idx} {dp[N][L]}")