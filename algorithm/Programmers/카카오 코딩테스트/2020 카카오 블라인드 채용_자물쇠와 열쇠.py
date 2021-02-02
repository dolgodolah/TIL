# 예전에 배열 회전 알고리즘 공부할 때 이 문제를 잠깐 보고 지나갔었다. (못풀거같아서)
# 배열을 90도 회전시키는 방법을 팀노트에 기록했었는데 이번 풀이에 도움이 됐다.

# 열쇠의 끄트머리 하나가 자물쇠에 삽입될 수도 있는 것이다.
# 그러므로 자물쇠와 열쇠의 크기를 고려하여 board라는 배열을 새로 만든다.
# 자물쇠가 아래 3x3배열과 같고 열쇠의 크기도 3x3일때 다음과 같이 board를 만든다.
#                 [0,0,0,0,0,0,0]
#                 [0,0,0,0,0,0,0]
# [1,1,1]         [0,0,1,1,1,0,0]
# [1,0,1]   ->    [0,0,1,0,1,0,0]
# [1,0,1]         [0,0,1,0,1,0,0]
#                 [0,0,0,0,0,0,0]
#                 [0,0,0,0,0,0,0]

# board배열을 순차적으로 탐색하여 열쇠가 꽂히는지, 자물쇠부분만 전부 1로 채워지는지 확인한다.
# 나같은 경우는 자물쇠 부분만 인덱싱하여 확인하는 부분이 잘못되어 애먹었다.
from copy import deepcopy
def solution(key, lock):
    board = [[0]*(len(lock)+2*(len(key)-1)) for _ in range(len(lock)+2*(len(key)-1))]
    
    # for i in key:
    #     print(i)
    # print()

    for i in range(len(lock)):
        for j in range(len(lock)):
            board[i+len(key)-1][j+len(key)-1]=lock[i][j]
    # for i in board:
    #     print(i)
    # print()

    def insert_key(x,y):
        temp_board = deepcopy(board)
        for i in range(len(temp_board)):
            for j in range(len(temp_board)):
                if i==x and j==y:
                    for xx in range(len(key)):
                        for yy in range(len(key)):
                            if temp_board[i+xx][j+yy]==1 and key[xx][yy]==1: #돌기끼리 부딪힌다.
                                return
                            if temp_board[i+xx][j+yy]==0 and key[xx][yy]==1:
                                temp_board[i+xx][j+yy]=1

        # for i in temp_board:
        #     print(i)
        # print()

        for i in range(len(key)-1,len(key)-1+len(lock)):
            for j in range(len(key)-1,len(key)-1+len(lock)):
                if temp_board[i][j]==0:
                    return
        return True
    for _ in range(4):
        # for i in key:
        #     print(i)
        for i in range(len(board)):
            for j in range(len(board)):
                if i+len(key)-1<len(board) and j+len(key)-1<len(board):
                    if insert_key(i,j):
                        return True
        key=list(zip(*key[::-1]))
    return False

print(solution([[1, 0, 0, 0], [0, 1, 0, 0],[0, 0, 0, 1],[0,0,1,0]],[[1, 0, 1], [0, 1, 1], [1, 1, 1]]))
