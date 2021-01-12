import sys
from collections import deque
input = sys.stdin.readline

graph = []
for _ in range(5):
    graph.append(list(input().split()))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
temp_answer = set()
def dfs(x,y,text):
    global temp_answer
    if len(text)>5:
        temp_answer.add(text)
        return
    for i in range(4):
        if 0<=x+dx[i]<5 and 0<=y+dy[i]<5:
            nx, ny = x+dx[i],y+dy[i]
            dfs(nx,ny,text+graph[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])

print(len(temp_answer))
