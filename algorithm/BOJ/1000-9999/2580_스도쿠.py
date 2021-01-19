# 95%쯤에서 시간초과가 발생했다.
# 최초 정답에서 멈추지 않고 계속 백트래킹을 수행해 다른 정답이 있는지 확인하는 과정때문에 그랬다.
# 그래서 최초정답 때 출력을 하기 위해서 sys.exit(0)을 통해 해당 정답 출력 후 바로 종료시켰다.

import sys
from copy import deepcopy
input = sys.stdin.readline
answer = []
graph = []
for _ in range(9):
    graph.append(list(map(int,input().split())))

pos=[] #숫자를 채울 칸의 위치와
total = 0 #숫자를 채울 칸의 갯수를 저장한다.
for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            pos.append((i,j))
            total+=1

def check(x,y,num): #해당 num가 들어갈 해당 칸(x,y)에 들어갈 수 있는지 확인하는 함수
    #가로줄 세로줄에 숫자 겹치는지 확인
    for i in range(9):
        if graph[x][i]==num or graph[i][y]==num:
            return False

    if 0<=x<3:
        if 0<=y<3: #좌상단 3x3
            for i in range(3):
                for j in range(3):
                    if graph[i][j]==num:
                        return False
        elif 3<=y<6: #상단 3x3
            for i in range(3):
                for j in range(3,6):
                    if graph[i][j]==num:
                        return False
        elif 6<=y<9: #우상단 3x3
            for i in range(3):
                for j in range(6,9):
                    if graph[i][j]==num:
                        return False
    elif 3<=x<6:
        if 0<=y<3: #좌측 3x3
            for i in range(3,6):
                for j in range(3):
                    if graph[i][j]==num:
                        return False
        elif 3<=y<6: #가운데 3x3
            for i in range(3,6):
                for j in range(3,6):
                    if graph[i][j]==num:
                        return False
        elif 6<=y<9: #우측 3x3
            for i in range(3,6):
                for j in range(6,9):
                    if graph[i][j]==num:
                        return False
    elif 6<=x<9:
        if 0<=y<3: #좌하단 3x3
            for i in range(6,9):
                for j in range(3):
                    if graph[i][j]==num:
                        return False
        elif 3<=y<6: #하단 3x3
            for i in range(6,9):
                for j in range(3,6):
                    if graph[i][j]==num:
                        return False
        elif 6<=y<9: #우하단 3x3
            for i in range(6,9):
                for j in range(6,9):
                    if graph[i][j]==num:
                        return False
    return True
def dfs(cnt):
    global answer
    if cnt==total: #빈 칸(0)을 다 채웠으면
        for i in range(9):
            for j in range(9):
                print(graph[i][j],end=" ")
            print()
        sys.exit(0) #시간 단축을 위해 최초정답 출력하고 종료한다.
        return
    x,y=pos[cnt]
    for i in range(1,10):
        if check(x,y,i): #해당 칸(x,y)에 i를 넣을 수 있으면
            graph[x][y]=i
            dfs(cnt+1)
        graph[x][y]=0

dfs(0)