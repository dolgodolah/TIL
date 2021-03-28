# 구현 문제 푸는데 시간이 너무 오래 걸린다.
# 주어진 데이터들을 어떻게 활용해야하는지가 중요하다.

# 체스판의 각 칸은 0,1,2로 각 칸의 상태를 나타내는 board 리스트
# 각 말들의 좌표,이동방향을 나타내는 horse 리스트
# 각 말들(인덱싱으로 표현)의 위치를 나타내는 MAP 리스트
from collections import deque
N,K=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
horse=[]
MAP=[[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    x,y,direction=map(int,input().split())
    horse.append((x-1,y-1,direction))
    MAP[x-1][y-1].append(i+1)
visited=[] # visited를 통해 같은 horse 리스트가 두 번 이상 반복되면 게임은 무한루프이다.
visited.append(list(horse))
dx=[0,0,0,-1,1] # →, ←, ↑, ↓
dy=[0,1,-1,0,0]
# for i in MAP:
#     print(i)
# print(horse)
# print()
cnt=0
def check():
    for i in range(N):
        for j in range(N):
            if len(MAP[i][j])>=4:
                return True
    return False

answer=0
while True:
    answer+=1
    for i in range(len(horse)):
        x,y,direction=horse[i][0],horse[i][1],horse[i][2]
        if MAP[x][y][0]!=i+1: # 해당 말이 가장 아래에 있지 않은 경우
            continue
        nx,ny=x+dx[direction],y+dy[direction]
        if not 0<=nx<N or not 0<=ny<N or board[nx][ny]==2: # 파란색이거나 체스판 벗어나는 경우
            # 방향을 반대로 한다.
            if direction==1:direction=2
            elif direction==2:direction=1
            elif direction==3:direction=4
            elif direction==4:direction=3
            nx,ny=x+dx[direction],y+dy[direction]
            idx=MAP[x][y][0]
            horse[idx-1]=(x,y,direction)
            if not 0<=nx<N or not 0<=ny<N or board[nx][ny]==2: # 방향을 바꾼 후에도 파란색이면
                # 이동방향만 바꿔준다.
                continue
                
        if board[nx][ny]==0: # 흰색
            while MAP[x][y]:
                idx=MAP[x][y].pop(0)
                MAP[nx][ny].append(idx)
                horse[idx-1]=(nx,ny,horse[idx-1][2]) # 이동방향은 각 말들의 이동방향 그대로 유지해야한다.
        elif board[nx][ny]==1: # 빨간색
            while MAP[x][y]:
                idx=MAP[x][y].pop()
                MAP[nx][ny].append(idx)
                horse[idx-1]=(nx,ny,horse[idx-1][2])
    # for i in MAP:
    #     print(i)
    # print(horse)
    # print()

    # 게임종료조건을 만족하는지 확인한다.
    if check():
        print(answer)
        break
    if answer>=1000: # 같은 경로를 또 간다는 것은 절대로 게임이 종료되지 않는다는 것이다.
        print(-1)
        break
    visited.append(list(horse))

