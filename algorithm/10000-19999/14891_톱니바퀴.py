import sys

def rotate(index,direction):
    if direction==1: #시계방향 회전
        temp = wheels[index][7]
        for i in range(7,0,-1):
            wheels[index][i]=wheels[index][i-1]
        wheels[index][0] = temp

    elif direction==-1: #반시계방향 회전
        temp = wheels[index][0]
        for i in range(7):
            wheels[index][i]=wheels[index][i+1]
        wheels[index][7] = temp

def set_wheels(index, idx_direction):
    left, right = [], [] #톱니바퀴들의 왼쪽 톱니, 오른쪽 톱니
    for wheel in wheels:
        left.append(wheel[6])
        right.append(wheel[2])
    val = [False] * 4 # 톱니바퀴들 회전 여부


    direction = idx_direction
    #선택한 톱니바퀴 회전 처리
    rotate(index-1,direction)
    val[index-1]=True

    #선택한 톱니바퀴 기준 오른쪽에 있는것들 회전 처리
    for i in range(index-1,3):
        if val[i]==True:
            if right[i] == left[i+1]:
                continue
            elif right[i] != left[i+1]:
                val[i+1]=True
                if direction==1:
                    rotate(i+1,-1)
                    direction=-1
                elif direction==-1:
                    rotate(i+1,1)
                    direction=1
    direction = idx_direction
    #선택한 톱니바퀴 기준 왼쪽에 있는것들 회전 처리
    for i in range(index-1,0,-1):
        if val[i]==True:
            if left[i] == right[i-1]:
                continue
            elif left[i] != right[i-1]:
                val[i-1]=True
                if direction==1:
                    rotate(i-1,-1)
                    direction=-1
                elif direction==-1:
                    rotate(i-1,1)
                    direction=1

def get_score():
    answer = 0
    for i in range(4):
        if wheels[i][0] != 0:
            if i==0:
                answer+=1
            elif i==1:
                answer+=2
            elif i==2:
                answer+=4
            elif i==3:
                answer+=8
    return answer

wheels = []
for _ in range(4):
    wheels.append(list(map(int,input())))
k = int(input())
moves = []
for _ in range(k):
    moves.append(list(map(int,input().split())))

for move in moves:
    set_wheels(move[0],move[1])#톱니바퀴번호, 회전방향


# print(wheels)
print(get_score())

