import sys
from copy import deepcopy
input = sys.stdin.readline
graph = []
for _ in range(10):
    graph.append(list(map(int,input().split())))
paper = [0]*6

def check(x,y,k,graph):
    #한 변의 길이가 k인 색종이가 값이 1인 부분만 정확히 덮는지 확인
    for i in range(x,x+k):
        for j in range(y,y+k):
            if not 0<=i<10 or not 0<=j<10 or graph[i][j]!=1: #다른 부분을 덮게 되거나 맵밖을 벗어나버리면 False
                return False
    
    #값이 1인 부분만 정확히 덮게 된다면 색종이로 덮고 True를 반환
    for i in range(x,x+k):
        for j in range(y,y+k):
            graph[i][j]=0
    return True

def dfs(x,y,graph):
    global answer
    #오른쪽 끝까지 다 돌았으면 아래로 한 칸 내린다.
    if y==10:
        dfs(x+1,0,graph)
        return
    
    #x==10인 경우는 그래프를 끝까지 검사한 경우이므로 이 때까지 사용한 색종이의 수를 구한다.
    if x==10:
        answer = min(sum(paper[1:6]),answer)
        return
    
    #해당 좌표가 색종이를 붙여야한다면
    if graph[x][y]==1:
        for k in range(5,0,-1):
            #5x5부터 1x1 색종이를 붙여본다.
            #특정 크기의 색종이 사용 횟수가 5보다 작아야한다. (최대 5장이므로)
            #graph[x][y]의 값이 1로 되어있는 부분만 덮어야하는데 이를 check 함수에서 확인한다.
            if paper[k]<5 and check(x,y,k,graph)==True:
                paper[k]+=1
                dfs(x,y+k,graph)
                paper[k]-=1
                for i in range(x,x+k):
                    for j in range(y,y+k):
                        graph[i][j]=1
    
    #해당 좌표의 값이 0이면 (x,y+1)의 값을 검사한다.
    else:
        dfs(x,y+1,graph)

answer = int(10e9)
dfs(0,0,graph)
if answer == int(10e9):
    print(-1)
else:
    print(answer)
