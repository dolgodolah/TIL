# 피보나치 점화식을 이용한 dp 풀이
def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[0],dp[1]=0,1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    answer=dp[n]%1234567
    return answer

print(solution(5))