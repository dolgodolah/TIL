# 주어진 데이터들을 통해서 BFS를 진행하여 조건에 따라 출력해주면 된다.
# X,Y의 개념이 평소 풀었던 방법과 반대로 주어져 좌표에 대한 처리에서 시간이 걸렸다.
# robots : 로봇들의 좌표값과 바라보고 있는 방향을 나타낸다.
# board : 격자에 상태를 나타낸다. 0은 빈공간, 1이상의 숫자는 로봇 인덱스를 나타낸다.

# dx,dy의 방향이 순서대로 '북,동,남,서'처럼 초기화해놓으면
# 오른쪽으로 회전시 (direction+1)%4를 하면 되고, 왼쪽 회전시 (direction+3)%4를 하면 된다.
import sys
from collections import deque
input=sys.stdin.readline
a,b=map(int,input().split())
n,m=map(int,input().split())
board=[[0]*a for _ in range(b)]
robots=list()
for i in range(n):
    x,y,command=input().split()
    robots.append([int(x),int(y),command])
    board[int(y)-1][int(x)-1]=i+1


commands=list()
for _ in range(m):
    idx,command,cnt=input().split()
    commands.append((int(idx),command,int(cnt)))
dx=[0,1,0,-1]
dy=[1,0,-1,0]
direction=['N','E','S','W'] #북,동,남,서

# def printBoard():
#     for i in range(len(board)-1,-1,-1):
#         print(board[i])
#     print(robots)
# printBoard()

def bfs(x,y):
    queue=deque()
    queue.append((x,y,direction.index(robots[idx-1][2])))
    for _ in range(cnt):
        x,y,d=queue.popleft()
        nx=x+dx[d]
        ny=y+dy[d]
        if not 0<=nx<a or not 0<=ny<b: #벽 충돌하는 경우
            print(f"Robot {idx} crashes into the wall")
            return False
        if board[ny][nx]!=0:#로봇끼리 충돌하는 경우
            print(f"Robot {idx} crashes into robot {board[ny][nx]}")
            return False
        else:
            queue.append((nx,ny,d))
            board[ny][nx]=board[y][x]
            board[y][x]=0
            robots[idx-1][0]=nx+1
            robots[idx-1][1]=ny+1
    return True
for i in range(len(commands)):
    idx,command,cnt=commands[i][0],commands[i][1],commands[i][2]
    if command=='R':
        robots[idx-1][2]=direction[(direction.index(robots[idx-1][2])+cnt)%4]
    elif command=='L':
        robots[idx-1][2]=direction[(direction.index(robots[idx-1][2])+cnt*3)%4]
    else:
        if not bfs(robots[idx-1][0]-1,robots[idx-1][1]-1):
            break
else:
    print("OK")
