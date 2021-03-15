# <	이동 방향을 왼쪽으로 바꾼다.
# >	이동 방향을 오른쪽으로 바꾼다.
# ^	이동 방향을 위쪽으로 바꾼다.
# v	이동 방향을 아래쪽으로 바꾼다.
# _	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
# |	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
# ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
# .	아무 것도 하지 않는다.
# @	프로그램의 실행을 정지한다.
# 0~9	메모리에 문자가 나타내는 값을 저장한다.
# +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
# -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.

from collections import deque
def bfs(x,y,memory,direction):
    queue=deque()
    queue.append((x,y,memory,direction))
    visited=set()
    visited.add((x,y,memory,direction))
    while queue:
        x,y,memory,direction=queue.popleft()
        # print(x,y,memory,direction)
        if board[x][y]=='<':
            direction=2
        elif board[x][y]=='>':
            direction=0
        elif board[x][y]=='^':
            direction=3
        elif board[x][y]=='v':
            direction=1
        elif board[x][y]=='_':
            if memory==0:
                direction=0
            else:
                direction=2
        elif board[x][y]=='|':
            if memory==0:
                direction=1
            else:
                direction=3
        elif board[x][y]=='?':
            for i in range(4):
                nx=(x+move[i][0])%r
                ny=(y+move[i][1])%c
                if not (nx,ny,memory,i) in visited:
                    visited.add((nx,ny,memory,i))
                    queue.append((nx,ny,memory,i))
            continue
        elif board[x][y]==".":
            memory = memory
        elif board[x][y]=='@':
            return True
        elif board[x][y] in ['1','2','3','4','5','6','7','8','9','0']:
            memory=int(board[x][y])
        elif board[x][y]=='+':
            if memory==15:
                memory=0
            else:
                memory+=1
        elif board[x][y]=='-':
            if memory==0:
                memory=15
            else:
                memory-=1
        nx=(x+move[direction][0])%r
        ny=(y+move[direction][1])%c
        if not (nx,ny,memory,direction) in visited:
            visited.add((nx,ny,memory,direction))
            queue.append((nx,ny,memory,direction))
    return False




move=[(0,1),(1,0),(0,-1),(-1,0)] #오른쪽, 아래, 왼쪽, 위
test_case=int(input())
for t in range(1,test_case+1):
    r,c=map(int,input().split())
    board=[]
    for _ in range(r):
        board.append(list(input()))

    if bfs(0,0,0,0):
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")