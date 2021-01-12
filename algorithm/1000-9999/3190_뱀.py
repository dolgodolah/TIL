import sys
from collections import deque
input = sys.stdin.readline
n = int(input()) #보드 크기
k = int(input()) #사과 개수
move=[(-1,0),(1,0),(0,-1),(0,1)]
apple = []
for _ in range(k):
    apple.append(list(map(int,input().split())))

l = int(input())
command = []
for _ in range(l):
    command.append(list(input().split()))
 
cnt = 0
def game():
    global cnt
    snake = deque()
    snake.append([1,1])
    _type = 3
    while 1<=snake[0][0]<=n and 1<=snake[0][1]<=n:
        if command and cnt == int(command[0][0]):
            direction = command.pop(0)[1]
            if direction=='D':
                if _type==0:_type=3
                elif _type==1:_type=2
                elif _type==2:_type=0
                elif _type==3:_type=1
            elif direction=='L':
                if _type==0:_type=2
                elif _type==1:_type=3
                elif _type==2:_type=1
                elif _type==3:_type=0

        #뱀의 머리를 다음칸에 위치시킨다.
        x,y = snake[0][0]+move[_type][0],snake[0][1]+move[_type][1]

        #자기자신의 몸에 부딪히면 게임 끝.
        if [x,y] in snake:
            cnt+=1
            break
        snake.appendleft([x,y])
        
        if snake[0] in apple:#이동한 칸에 사과가 있다면 그 칸에 있던 사과 없어진다.
            apple.remove(snake[0])
        else:#사과가 없다면 몸길이를 다시 줄인다.
            snake.pop()

        # print(snake)
        cnt+=1
game()
print(cnt)