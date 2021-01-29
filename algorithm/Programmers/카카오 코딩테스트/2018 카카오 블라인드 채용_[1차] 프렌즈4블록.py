# board 전체를 탐색해 2x2 크기의 같은 블럭을 찾아 처리한다.
# 깨진 블럭을 ' '로 바꿔주고 위에 안깨진 블럭이 있으면 내려오도록 구현한다.

dx=[0,0,1,1]
dy=[0,1,0,1]

def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i]=list(board[i])
    visited = [[False]*n for _ in range(m)]
    while True: #깨지는 블럭이 없을 때까지 진행한다.
        val=False #while문을 종료시킬지 결정하는 변수

        #2x2모양의 같은 4개 블럭(깨질 블럭)을 찾아 visited를 True로 바꿔준다.
        for x in range(m-1):
            for y in range(n-1):
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    if board[x][y]==' ' or board[x][y]!=board[nx][ny]:
                        break
                else: #2x2모양의 4개 블록 발견하면
                    for i in range(4):
                        nx,ny=x+dx[i],y+dy[i]
                        if visited[nx][ny]==False:
                            visited[nx][ny]=True
                            val=True
                            answer+=1

        if val==False:break
            
        #visited를 통해 깨질 블럭을 ' '로 바꿔준다.
        for i in range(m):
            for j in range(n):
                if visited[i][j]==True:
                    visited[i][j]=False
                    board[i][j]=' '


        #' ' 위에 남아있는 블럭이 있으면 내려온다.
        for i in range(m-1,0,-1):
            for j in range(n):
                if board[i][j]==' ':
                    for k in range(1,i+1):
                        if not board[i-k][j]==' ':
                            board[i][j],board[i-k][j]=board[i-k][j],' '
                            break
        


    

    return answer

print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6,6,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
print(solution(4,5,['AAAAA','AUUUA','AUUAA','AAAAA']))