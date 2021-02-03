# 하단에 주석처리한 소스 코드는 처음에 푼 풀이로 완전탐색 -> 효율성 테스트에서 0점을 맞은 코드이다.
# dp 점화식을 생각해내기가 아직 어렵다. dp 문제를 따로 공부하고 다시 풀어봐야겠다.


def solution(board):
    answer =0
    N,M=len(board),len(board[0])
    for i in range(1,N):
        for j in range(1,M):
            if board[i][j]==1:
                board[i][j]=min(board[i-1][j-1],board[i][j-1],board[i-1][j])+1

    for i in range(N):
        for j in range(M):
            answer = max(board[i][j],answer)
    return answer**2
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,0,0]]))
print(solution([[1,0],[0,0]]))



# def solution(board):
#     answer = 0
#     N,M=len(board),len(board[0])

#     def get_max(x,y):
#         cnt = 1
#         while True:
#             for i in range(x,x+cnt):
#                 for j in range(y,y+cnt):
#                     if not 0<=i<N or not 0<=j<M or not board[i][j]==1:
#                         return (cnt-1)**2
#             cnt+=1
            
#     for i in range(N):
#         for j in range(M):
#             answer = max(answer,get_max(i,j)) #해당 좌표(i,j)에서 만들수 있는 최대 정사각형 넓이를 구한다.

#     return answer
