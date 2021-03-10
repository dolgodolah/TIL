# 땅을 언제 파야하고 언제 채워야하지...하다가
# 탐색 범위가 최대 500*500*256이므로 브루트포스로 해결 가능하다는걸 알았다.
# 목표 높이를 정해놓고 모든 땅을 해당 높이로 만드는 것이다.
# 해당 높이로 만들고 나서 인벤토리에 있는 블럭 개수가 음수이면 해당 땅 높이는 만들 수 없는 것이다.

import sys
input=sys.stdin.readline
n,m,b=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]


def solution(h,block_number): #목표높이, 인벤토리의 블럭 수
    sec=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==h:
                continue
            elif board[i][j]>h: #땅을 파야할 때
                sec+=(board[i][j]-h)*2
                block_number+=board[i][j]-h
            elif board[i][j]<h: #땅을 채워야할 때
                sec+=h-board[i][j]
                block_number=block_number-(h-board[i][j])
            if sec>answer_t: #최소시간보다 이미 sec가 커버리면 그만!
                return -1
    if block_number<0:
        return -1
    else:
        return sec
                

answer_t=int(10e9)
answer_h=0
for i in range(256,-1,-1): # 최소시간이 여러개인 경우 땅의 높이가 높은 것을 출력하기 위해 내림차순으로 탐색
    sec=solution(i,b) #solution(목표높이, 인벤토리의 블럭 수)
    if sec>=0:
        if answer_t>sec:
            answer_t=sec
            answer_h=i
print(answer_t,answer_h)