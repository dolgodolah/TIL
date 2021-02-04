# dp로 쉽게 구현할 수 있는 문제이다. 괜히 한번 dfs로 풀고 시간초과 뜨는거 보고싶어서 dfs풀이도 밑에 주석처리해놨다.
# 자꾸 1,000,000,007로 나눈 나머지를 반환하라는 제한사항을 잊어버리는데 주의하자.

def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles or (i==1 and j==1):
                continue
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    
    answer = dp[n][m]
    return answer

# dx = [0,1]
# dy = [1,0]
# answer = 0
# def solution(m, n, puddles):
#     global answer
#     answer = 0
#     board = [[0]*(m) for _ in range(n)]
#     for puddle in puddles:
#         board[puddle[1]-1][puddle[0]-1]=1

#     visited = [[False]*m for _ in range(n)]
#     def dfs(x,y):
#         global answer
#         visited[x][y]=True
#         if x==n-1 and y==m-1:
#             answer+=1
#             return
#         for i in range(2):
#             nx,ny=x+dx[i],y+dy[i]
#             if nx<n and ny<m:
#                 if board[nx][ny]!=1 and visited[nx][ny]==False:
#                     dfs(nx,ny)
#                     visited[nx][ny]=False
#     dfs(0,0)
#     return answer%1000000007

print(solution(4,3,[[2,2]]))
print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
