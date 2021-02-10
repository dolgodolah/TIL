n,m=map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input())))

dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            if i==0 or j==0:
                dp[i][j]=board[i][j]
                continue
            dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
answer = 0
for i in dp:
    answer=max(max(i),answer)
print(answer*answer)