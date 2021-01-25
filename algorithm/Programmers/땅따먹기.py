def solution(land):
    answer = 0
    dp = [[0]*4 for _ in range(len(land))]
    for i in range(4):
        dp[0][i]=land[0][i]

    for i in range(1,len(land)):
        for j in range(4):
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j-2],dp[i-1][j-3])+land[i][j]
    answer = max(dp[len(land)-1])
    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1],[4,3,2,1]]))
print(solution([[9,5,2,3],[9,8,6,7],[8,9,7,1],[100,9,8,1]]))
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))