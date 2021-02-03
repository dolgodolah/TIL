# 이런 DP문제는 쉽지요 ^^~
# 삼각형으로 주어진 리스트를 사각형 리스트로 바꿔 생각하자.
# [[7],                             [7, 0, 0, 0, 0]
#  [3, 8],                          [3, 8, 0, 0, 0]
#  [8, 1, 0],           ->          [8, 1, 0, 0, 0]
#  [2, 7, 4, 4],                    [2, 7, 4, 4, 0]
#  [4, 5, 2, 6, 5]]                 [4, 5, 2, 6, 5]

# [i-1][j]와 [i-1][j-1]의 누적합 중 더 큰 것을 골라 [i][j]를 갱신하면 된다.
# 주의할 점은 j=0인 부분만 예외처리해주면 된다.
def solution(triangle):
    answer = 0
    dp = [[0]*len(triangle) for _ in range(len(triangle))]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j]=triangle[i][j]
    
    for i in range(1,len(dp)):
        for j in range(len(dp[i])):
            if j==0:
                dp[i][j]=dp[i-1][j]+dp[i][j]
            else:
                dp[i][j]=max(dp[i-1][j]+dp[i][j],dp[i-1][j-1]+dp[i][j])

    answer = max(dp[len(dp)-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))