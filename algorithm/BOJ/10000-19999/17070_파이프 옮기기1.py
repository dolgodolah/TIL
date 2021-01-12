from collections import deque
n = int(input())
graph = []

#→, ↘, ↓
dx = [0,1,1] 
dy = [1,1,0]

for i in range(n):
    graph.append(list(map(int,input().split())))


answer = 0
def dfs(x,y,pipe_type): #pipe_type 0(가로), 1(세로), 2(대각)
    global answer
    if x==n:
        return
    elif x==n-1 and y==n-1:
        answer+=1
        return
    else:
        if pipe_type==0: #파이프가 가로일 때
            if y+1<n and graph[x][y+1]==0:
                graph[x][y+1]=1
                dfs(x,y+1,0)
                graph[x][y+1]=0
            if y+1<n and x+1<n and graph[x+1][y+1]==0 and graph[x+1][y]==0 and graph[x][y+1]==0:
                graph[x+1][y+1]=1
                dfs(x+1,y+1,2)
                graph[x+1][y+1]=0
        elif pipe_type==1: #파이프가 세로일 때
            if x+1<n and graph[x+1][y]==0:
                graph[x+1][y]=1
                dfs(x+1,y,1)
                graph[x+1][y]=0
            if x+1<n and y+1<n and graph[x+1][y+1]==0 and graph[x+1][y]==0 and graph[x][y+1]==0:
                graph[x+1][y+1]=1
                dfs(x+1,y+1,2)
                graph[x+1][y+1]=0
        elif pipe_type==2: #파이프가 대각일 때
            if y+1<n and graph[x][y+1]==0:
                graph[x][y+1]=1
                dfs(x,y+1,0)
                graph[x][y+1]=0
            if x+1<n and graph[x+1][y]==0:
                graph[x+1][y]=1
                dfs(x+1,y,1)
                graph[x+1][y]=0
            if x+1<n and y+1<n and graph[x+1][y+1]==0 and graph[x+1][y]==0 and graph[x][y+1]==0:
                graph[x+1][y+1]=1
                dfs(x+1,y+1,2)
                graph[x+1][y+1]=0

dfs(0,1,0)
print(answer)
