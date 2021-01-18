# N,M의 크기가 최대 15이기 때문에 완전탐색을 해도 시간초과는 뜨지않았다.
# 문제 조건이 까다로워서 구현하기가 힘들었다.
# dfs함수를 통해서 십자가 2개를 놓을 수 있는 모든 조합을 구한다.
# 십자가가 2개가 되면 getMaxCross를 통해 두 십자가의 size가 몇까지 커질 수 있는지 구하고,
# 그게 최댓값이면 answer을 갱신한다.


from collections import deque
from copy import deepcopy


dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

def getMaxCross(temp,temp_graph): # 해당 두 좌표에 있는 십자가가 최대한 커질 수 있는만큼 증가.
    queue = deque()
    result = 1 #십자가 넓이의 곱의 최댓값을 구하기 때문에 초기값은 1로 해준다.
    for x,y in temp:
        queue.append((x,y,0))
    while queue:
        x,y,size = queue.popleft()
        cnt=0
        for i in range(4):
            nx = x+dx[i]*(size+1)
            ny = y+dy[i]*(size+1)
            if 0<=nx<n and 0<=ny<m:
                if temp_graph[nx][ny]=='#':
                    cnt+=1
        if cnt==4: #십자가가 올바르게 커질 수 있으면
            queue.append((x,y,size+1))
            for i in range(4):
                nx = x+dx[i]*(size+1)
                ny = y+dy[i]*(size+1)
                temp_graph[nx][ny]='*'
        else: #십자가가 더 이상 커질수 없으면 해당 좌표 십자가의 넓이를 곱해준다.
            result*=(size*4+1)
    return result


def dfs(cnt,start_i,start_j):
    global answer
    if cnt==2: #십자가 놓을 자리 두 곳 정하면 두 좌표에서 최대로 될 수 있는 십자가를 구한다.
        temp_graph=deepcopy(graph)
        temp = []
        #두 십자가의 좌표값을 구한다.
        for i in range(n):
            for j in range(m):
                if graph[i][j]=='*':
                    temp.append((i,j))
        answer = max(answer,getMaxCross(temp,temp_graph))
        return
    
    for i in range(start_i,n):
        for j in range(start_j,m):
            if graph[i][j]=='#':
                graph[i][j]='*'
                dfs(cnt+1,i,j+1)
                graph[i][j]='#'
        start_j=0

n,m = map(int,input().split())
graph=[]
for i in range(n):graph.append(list(input()))
dfs(0,0,0)
print(answer)