from collections import deque
king, stone, n = input().split()
n = int(n)

move_type = ['LT','T','RT','L','R','LB','B','RB']
move = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

commands = []
for _ in range(n):
    commands.append(input())

def move(kx,ky,sx,sy):
    queue = deque(commands)
    while queue:
        command = queue.popleft()
        for i in range(8):
            #해당 명령에 대해 움직임을 수행한다.
            if move_type[i]==command:
                if 0<=kx+move[i][0]<8 and 0<=ky+move[i][1]<8:
                    kx += move[i][0]
                    ky += move[i][1]
                    #킹을 움직였는데 돌의 위치랑 같게되면
                    if kx==sx and ky==sy:
                        #돌도 같은 방향으로 움직여주는데
                        if 0<=sx+move[i][0]<8 and 0<=sy+move[i][1]<8:
                            sx = sx + move[i][0]
                            sy = sy + move[i][1]
                        #돌이 체스판 밖으로 벗어나면 킹 움직임도 취소한다.
                        else:
                            kx -= move[i][0]
                            ky -= move[i][1]
    return kx,ky,sx,sy


#킹의 체스판 위치값을 배열 좌표값으로 바꾼다. ex) A1 -> (7,0)
kx= 8-int(king[1])
ky = ord(king[0])-ord('A')

#돌의 체스판 위치값을 배열 좌표값으로 바꾼다. ex) A8 -> (0,0)
sx = 8-int(stone[1])
sy = ord(stone[0])-ord('A')

#입력받은 명령에 대해 move를 수행 한 후의 좌표값들을 구한다.
kx,ky,sx,sy = move(kx,ky,sx,sy)

#배열 좌표값을 체스판 위치로 바꾼다.
kx,ky = 8-kx,chr(ky+ord('A'))
sx,sy = 8-sx,chr(sy+ord('A'))

answer1 = str(ky)+str(kx)
answer2 = str(sy)+str(sx)
print(answer1)
print(answer2)