# 예제에서 주어진 *를 보고 만들 수 있는 십자가들을 찾는게 아니라
# 십자가들로 해당 예제를 만들 수 있는지 없는지를 찾아내야한다.

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y):
    global visited
    cnt = 0 # 십자가 길이
    val = True
    while val:
        cnt+=1
        for i in range(4):
            if 0<=x+dx[i]*cnt<n and 0<=y+dy[i]*cnt<m:
                nx = x+dx[i]*cnt
                ny = y+dy[i]*cnt

                if graph[nx][ny]!='*': #상하좌우 중 하나라도 *가 아니면 길이 cnt만큼의 십자가를 만들 수 없다.
                    val = False
                    break
            else: #맵밖을 벗어나면 길이 cnt만큼의 십자가를 만들 수 없다.
                val = False
                break
            if i==3: #길이 cnt만큼의 십자가를 만들 수 있다면
                visited[x][y],visited[x-cnt][y],visited[x+cnt][y],visited[x][y-cnt],visited[x][y+cnt]=False,False,False,False,False
                answer.append([x+1,y+1,cnt]) #정답리스트에 추가한다.
    
            



n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))

# 주어진 예제와 같은 리스트 하나를 만든다.
# 마지막에 정답을 출력할 때 이 visited에 True가 있다면, 즉 십자가들로 해당 예제를 만들 수 없다면 -1를 출력할 것이다.
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]=='*':
            visited[i][j]=True

answer = []
for i in range(n):
    for j in range(m):
        # (i,j)를 중심으로 십자가를 만들 수 있는지 없는지 check한다.
        if graph[i][j]=='*':
            check(i,j)


for i in range(n):
    if True in visited[i]: # visited에 True가 남아있다면 -1를 출력한다.
        print(-1)
        break
    if i==n-1: # visited에 True가 없다면 정답을 출력한다.
        print(len(answer))
        for i in range(len(answer)):
            print(*answer[i])
