import sys
from collections import deque
input=sys.stdin.readline

R,C,N=map(int,input().split())
board=list()
for _ in range(R):
    board.append(list(input().strip()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bomb():
    for x,y in old_bomb:
        board[x][y]='.'
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<R and 0<=ny<C:
                board[nx][ny]='.'

def putBomb():
    for i,j in new_bomb:
        board[i][j]='O'

N-=1
while True:
    if N<=0:break
    old_bomb=list()
    for i in range(R):
        for j in range(C):
            if board[i][j]=='O':
                old_bomb.append((i,j))

    new_bomb=list()
    for i in range(R):
        for j in range(C):
            if board[i][j]=='.':
                new_bomb.append((i,j))
    N-=1
    putBomb()

    if N<=0:
        break

    N-=1
    bomb()
 
    if N<=0:
        break


for i in board:
    print(''.join(i))