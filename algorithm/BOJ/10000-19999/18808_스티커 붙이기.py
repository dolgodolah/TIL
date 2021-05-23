n,m,k=map(int,input().split())
board=[[0]*m for _ in range(n)]
stickers=[[] for _ in range(k)]
for i in range(k):
    r,c=map(int,input().split())
    for _ in range(r):
        stickers[i].append(list(map(int,input().split())))

# 스티커를 노트북에 붙일 수 있는지 판단한다.
def check(x,y,sticker):
    # 노트북의 위쪽부터 스티커를 채워 나가려고 해서,
    # 스티커를 붙일 수 있는 위치가 여러 곳 있다면 가장 위쪽의 위치를 선택한다.
    # 가장 위쪽에 해당하는 위치도 여러 곳이 있다면 그중에서 가장 왼쪽의 위치를 선택한다.
    
    # 라는 조건때문에 좌상단부터 탐색하면 된다.

    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]==1: # 스티커[i][j]가 스티커가 있는 공간이라면
                if 0<=i+x<n and 0<=j+y<m: # 노트북 밖을 벗어나지 않고
                    if board[i+x][j+y]==0: # 노트북[i+x][j+y]가 빈 공간이어야 붙일 수 있다.
                        continue
            else: # 스티커[i][j]가 빈공간이면 노트북[i+x][j+y]의 공간 여부에 상관없이 continue한다.
                continue
            return False # 위 조건문을 만족하지 못하면 스티커를 붙일 수 없다
    return True # 위 조건문을 sticker의 모든 좌표에서 만족하면 스티커를 붙일 수 있다.

# 스티커를 붙일 수 있다고 판단하면 stick()을 통해 board를 1로 채운다.
def stick(x,y,sticker,board):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]==1:
                board[i+x][j+y]=1

for sticker in stickers:
    val=False
    for _ in range(4):
        for i in range(n):
            for j in range(m):
                if check(i,j,sticker):
                    stick(i,j,sticker,board)
                    val=True
                    break
            if val:
                break
        if val:
            break
        sticker=list(zip(*sticker[::-1])) # 해당 스티커를 90도 회전시킨다.
        
answer=0
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            answer+=1
print(answer)