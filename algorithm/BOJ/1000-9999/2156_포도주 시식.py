# 세 잔을 연속해서 마실 수 없다는걸 유의하고, count에 연속으로 마신 횟수를 카운팅한다.
# 두 잔을 연속해서 마신 상태일 때
# 1. 이번 잔을 마시지 않을 경우 dp[i-1]
# 2. 전에 마셨던 잔을 마시지 않고 이번 잔을 마실 경우 dp[i-2]+wine[i]
# 3. 전전에 마셨던 잔을 마시지 않고 이번 잔을 마실 경우 dp[i-3]+wine[i-1]+wine[i]
# 이렇게 세 경우가 있는데 이 중 최대값을 dp에 넣고
# 경우에 따라 count를 적절히 설정해주면 된다.

n=int(input())
wine=[0]
for _ in range(n):
    wine.append(int(input()))

dp=[0]*(n+1)
dp[1]=wine[1]
count=1
for i in range(2,n+1):
    if count==2:
        dp[i]=max(dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-1])
        if dp[i]==dp[i-2]+wine[i]:
            count=1
        elif dp[i]==dp[i-3]+wine[i-1]+wine[i]:
            count=2
        else:
            count=0
    else:
        dp[i]=dp[i-1]+wine[i]
        count+=1
print(dp[n])
